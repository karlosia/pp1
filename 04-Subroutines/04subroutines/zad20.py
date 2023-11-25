def read_number():
    n=int(input("Enter a number: "))
    return n

if __name__ == "__main__":
    num1=read_number()
    num2=read_number()

print(f'{num1}+{num2}={num1+num2}')

