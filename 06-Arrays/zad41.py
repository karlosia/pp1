first_array=[2,3,4,5,6,7]
second_array=[1,2,3,4,5,6,7,8]
i=0
new_array=[]
for i in first_array:
    if i in second_array:
        new_array.append(i)
        i=i+1

if len(new_array)==len(first_array):
    print(True)
else:
    print(False)        
      
        

