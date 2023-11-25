a=input("Enter credit card number: ")

if len(a)==16:
    a1=(a[0:4])
    a2=(a[4:8])
    a3=(a[8:12])
    a4=(a[12:16])

    print(f'Card number: {a1} {a2} {a3} {a4}')