icao={"A":"Alfa",
      "B":"Bravo",
      "C":"Charlie",
      "D":"Delta",
      "Z":"Zulu"
}

with open('ICAO.txt','w') as file:
    for key, value in icao.items():
        file.write(f'{key}: {value}\n')