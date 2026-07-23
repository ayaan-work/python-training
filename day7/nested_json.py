import json

with open("day7/details.json", "r") as f:
    data=json.load(f)

print(data)
print(data["address"]["city"])
print(data["skills"])
print(data["skills"][0])

