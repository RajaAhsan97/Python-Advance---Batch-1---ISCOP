import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry
import requests

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

city = input("Enter city name: ")

# code to get latitude and logitude of city
geo_url = "https://geocoding-api.open-meteo.com/v1/search"

geo_params = {
	"name": city,
	"count": 1,
	"language": "en",
	"format": "json"
}

geo_response = requests.get(
	geo_url, params=geo_params, timeout=10
)
geo_response.raise_for_status()

geo_data = geo_response.json()
# print(geo_data)

# Step 2: Check whether the city exists
if not geo_data.get("results"):
	print("City not found.")

place = geo_data["results"][0]

latitude = place["latitude"]
longitude = place["longitude"]

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": latitude,
	"longitude": longitude,
	"current": ["temperature_2m", "wind_speed_10m", "relative_humidity_2m", "apparent_temperature", "pressure_msl"],
}
responses = openmeteo.weather_api(url, params = params)
print(responses[0])

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation: {response.Elevation()} m asl")
print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

# Process current data. The order of variables needs to be the same as requested.
current = response.Current()
current_temperature_2m = current.Variables(0).Value()
current_wind_speed_10m = current.Variables(1).Value()
current_relative_humidity_2m = current.Variables(2).Value()
current_apparent_temperature = current.Variables(3).Value()
current_sealevel_pressure = current.Variables(4).Value()

print(f"\nCurrent time: {current.Time()}")
print(f"Current temperature_2m: {current_temperature_2m}")
print(f"Current wind_speed_10m: {current_wind_speed_10m}")
print(f"Current relative_humidity_2m: {current_relative_humidity_2m}")
print(f"Current apparent_temperature: {current_apparent_temperature}")
print(current_sealevel_pressure)