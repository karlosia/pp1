import random

dice=random.randint(1,6)

guess=int(input("Enter a number from 1 to 6: "))

if guess==dice:
    print(f'True')
else:
    print(f'False')     
