def sum_of_the_digits(number, even):
    digits = [int(digit) for digit in str(number)]

    if even:
        return sum(d for d in digits if d % 2 == 0)
    else:
        return sum(d for d in digits if d % 2 != 0)

number = int(input('Enter your number: '))
even = input('Enter True if you want to sum even digits, or False for odd digits: ').lower() == 'true'
result = sum_of_the_digits(number, even)
print(result)
        