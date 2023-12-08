arr=[2,3,2,5,8,1,9,8]
unique=[]
not_unique=[]
for index in arr:
    if arr.count(index)>1:  
        not_unique.append(index)
        
for index in arr:
    if index not in not_unique:
        unique.append(index)
        
result=' '.join(map(str, unique))        



print(result)