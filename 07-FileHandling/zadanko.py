import csv

with open('studentslist.txt','r') as file:
    data=csv.reader(file)
    header=next(data)

    for row in data:
        age=row[2]
        if int(age)<30:
            print(row[0], row[1], row[4])
