import random

dice=random.randint(1,6)
print(f'Random dice is {dice}')

if dice==1 or dice==6:
    print(f'Special number: True')
else:
    print(f'Special number: False')     