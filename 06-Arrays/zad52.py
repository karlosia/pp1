arr=[[2,3,4,5,1],[6,3,1,8,9],[3,2,6,0,2]]

for row in arr:
    print(*row)

print('***AFTER SWAP***')
for i, row in enumerate(arr):
    arr[i][0],arr[i][-1]=arr[i][-1],arr[i][0]

for row in arr:
    print(*row)        

