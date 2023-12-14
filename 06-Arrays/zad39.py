array_of_numbers=[2,3,4,5,6]

evens=[]
odds=[]
i=0
for i in array_of_numbers:
    if i%2==0:
        evens.append(i)
    else:
        odds.append(i)
    i+=1
new_array=evens+odds

print(new_array)

