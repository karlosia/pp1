amount=int(input("Enter the amount in PLN: "))

if amount<0:
    print("Your number is not natural.")

five=amount//5
reszta=amount%5

two=reszta//2
reszta=reszta%2

one=reszta//1

print(f'The amount in PLN: {amount}')
print(f'\n5 zł - {five}, 2zł - {two}, 1 zł - {one} ')