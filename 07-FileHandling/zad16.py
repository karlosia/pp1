a=input('Enter your file name: ')
number_of_lines=0
f=open(a)

for line in f:
    number_of_lines+=1

print(f'Number of lines: {number_of_lines}')    
    