def different(n1,n2,n3):
    if n1==n2==n3:
        return 'are the same' 
    else:
        return 'are different'

n1=int(input('Enter the first number: '))
n2=int(input('Enter the second number: ')) 
n3=int(input('Enter the third number: '))

print(f'Numbers {n1}, {n2} and {n3} {different(n1,n2,n3)}.')