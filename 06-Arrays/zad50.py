arr=[[-38,19],[5,40],[-7,11],[29,16]]

small_value=0
large_value=0
small_value_location=[]
large_value_location=[]

for i, row in enumerate(arr):
    for j, value in enumerate(row):
        if value<small_value:
            small_value=value
            small_value_location=[i,j]
        elif value>large_value:
            large_value=value
            large_value_location=[i,j]


print(small_value)
print(small_value_location)
print(large_value)    
print(large_value_location)        
