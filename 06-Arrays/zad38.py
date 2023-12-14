a=int(input('Enter your value: '))

greater_elements=[]

array_of_numbers=[2,3,4,5,6]

i=0
for i in array_of_numbers:
    if i>a:
        greater_elements.append(i)
    i+=1

print(len(greater_elements))        