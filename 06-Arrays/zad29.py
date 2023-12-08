arr1=[4,36,12,28,9,44,5]
arr2=[5,1,36]

new_arr=[]

for index in arr1:
    if index not in arr2:
        new_arr.append(index)


print(new_arr)