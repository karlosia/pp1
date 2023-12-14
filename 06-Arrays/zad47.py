two_dimensional_array = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]


result=0

for element in two_dimensional_array[3]:
    result=element+result

print(result)    