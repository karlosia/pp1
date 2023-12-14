import json
import csv

with open('products.csv','r') as file:
    csv_reader=csv.reader(file)
    headers=next(csv_reader)
    data=[dict(zip(headers,row)) for row in csv_reader]

with open('products.json','w') as jsonfile:
    json.dump(data,jsonfile,indent=2)   

