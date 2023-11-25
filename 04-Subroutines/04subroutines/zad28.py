def binary_number(number):
    return all(char in {'1','0'} for char in number)

number=str(input("Enter to check if number is binary: "))

print(binary_number(number))
