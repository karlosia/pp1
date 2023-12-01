person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }


#a
print(person)
#b

print(person["name"])

#c
print(person["hobby"])

#d

person["surname"]="Nowak"

print(person["surname"])

#e

person["married"]= not person["married"]

#f

person["gender"]='male'

print(person)

#g

person["phone"]["work"]="123"
print(person)

