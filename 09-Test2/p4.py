def f(subjects):
    best_grade=0
    best_grade_key=""
    for key,value in subjects.items():
        if sum(value)/len(value)>best_grade:
            best_grade=sum(value)/len(value)
            best_grade_key=key

    return best_grade_key        

    
print(f({"math":[3,4,4],"geo":[5,4,5],"comp":[5,4]}))    