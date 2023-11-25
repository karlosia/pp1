phone_number=(input('Enter phone number: '))

if len(phone_number)==9:
    a=(phone_number[0:3])
    b=(phone_number[3:6])
    c=(phone_number[6:9])
    
    
    print(f'{a}-{b}-{c}')