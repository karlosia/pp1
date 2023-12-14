import json

with open('students.json','r') as first:
    data = json.load(first)


limited_students_data=[
    {
        'first_name':student['name'].split()[0],
        'last_name':student['surname'],
        'student ID':student['student ID']
    }
    for student in data
]

with open('limited.json','w') as second:
    json.dump(limited_students_data,second,indent=2)
