arr=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(5):
    for j in range(5):
        arr[i][j]=(1+i)*(1+j)

for row in arr:
    for value in row:
        print(f'{value:2d}', end=' ')
    print()    

