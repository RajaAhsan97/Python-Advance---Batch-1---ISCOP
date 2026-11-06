import json

with open("reviews.json", mode="r") as file:
    data = json.load(file)

verified_reviews = []
for product in data:
    #print(product.get("verified"))
     if product.get("verified")  is True:
         verified_reviews.append(product)

print(verified_reviews)

with open("verified_reviews.json", mode="w") as file:
    json.dump(verified_reviews, file)