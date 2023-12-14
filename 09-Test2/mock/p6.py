def f(years,course):
    import json
    with open("data.json",'r') as file:
        students=json.load(file)

    matching_students=[
        student for student in students
        if student.get('age',0)>=years and course in student.get and sum(course['grades'])/len(course['grades'])>=4
    ]

    return len(matching_students)

print(f(21,"statistics"))    
        
