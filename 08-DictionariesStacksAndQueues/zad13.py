data={"age": 34,
    "eyeColor": "blue",
    "name": {
        "first":"Stone",
        "last":"Douglas"
        },
    "gender": "male",
    "In company": True,}

number_of_pairs=0
for key,value in data.items():
    number_of_pairs+=1

print(number_of_pairs)    
