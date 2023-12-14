def f(subjects):
    highest_grade=0
    highest_subject=""
    for key,value in subjects.items():
        if sum(value)/len(value)>highest_grade:
            highest_grade=sum(value)/len(value)
            highest_subject=key

    return highest_subject    


print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))
            
