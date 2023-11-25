height=int(input('Enter your height in cm: '))
weight=int(input('Enter your weight in kg: '))

height_in_meters=height/100

BMI=weight/height_in_meters**2

print(f'Your BMI index is {BMI}')

if 18.5 <= BMI <= 24.99:
    print(f'Correct weight: True ')
else:
    print(f'Correct weight: False ')      