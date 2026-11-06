# JSON

# {
#     "name": "Ahsan",
#     "age": 30,
#     "course": "Python Advance",
#     "city": "Karachi"
# }

# {
#     "Teacher": {
#         "name": "Ahsan",
#         "age": 31
#     }
#     "skills": ["Python", "SQL", "Machine Learning", "COmputer vision"],
#     "active": True
# }

import json
# read json
# write json file
# JSON ko Python data convert
# Python --> JSON me convert kr sakty hein

# with open("user.json", mode="r") as file:
#     data  = json.load(file)

# print(data)

# print(data["name"])
# print(data["age"])
# print(data["city"])

# with open("users.json", mode="r") as file:
#     users  = json.load(file)

# for user_data in users:
#     print(f"User: {user_data['name']}")
#     print("SKills:")
#     print(f"{user_data['skills']}") 
#     print(f"Location: {user_data['city']}")


# with open("profile.json", mode="r") as file:
#     profile = json.load(file)

# print(profile["user"]["name"])
# print(profile["user"]["location"]["city"])
# print(profile["active"])
# #print(profile["user"]["phone"])
# print(profile["user"].get("phone", "Not provided"))

user = {
    "name": "Ahsan",
    "age": 30,
    "course": "Python Advance",
    "city": "Karachi"
}

with open("output_user.json", mode="w") as file:
    json.dump(user, file)