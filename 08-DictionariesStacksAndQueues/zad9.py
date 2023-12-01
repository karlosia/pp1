countries=[
    {"name":"Poland", "population":38000000},
    {"name":"Spain", "population":5000000},
    {"name":"USA", "population":120000000},
    {"name":"Canada", "population":90000000},
    {"name":"Germany", "population":70000000}

]


print("COUNTRY POPULATION")
i=0

while i<len(countries):
    print(f'{countries[i]["name"]} {countries[i]["population"]}')
    i+=1
    