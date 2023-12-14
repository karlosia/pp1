arr=[[2,3,4,5,1],[6,3,1,8,9],[3,2,6,0,2]]

for row in arr:
    print(*row)   


print('***AFTER A SWAP***')

arr[0],arr[-1]=arr[-1],arr[0]

for row in arr:
    print(*row)