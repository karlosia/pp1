import csv

with open('studentslist.txt','r') as file:
    csv_reader=csv.reader(file)

    header=next(csv_reader)

    for row in csv_reader:
        age=int(row[2])
        if age<30:
            print(f'{row[0]}  {row[1]}  {row[4]}')
                
        