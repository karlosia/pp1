arr=[-15,8,-31,47,-2,19]

min=arr[0]
max=arr[0]
for num in arr:
    if num>max:
        max=num
    elif num<min:
        min=num
        
        
print(max)
print(min)