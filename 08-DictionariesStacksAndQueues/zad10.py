import json

with open("generated.json") as file:
    data = json.load(file)

for key,value in data.items():
    print(f"{key} : {value}")
   