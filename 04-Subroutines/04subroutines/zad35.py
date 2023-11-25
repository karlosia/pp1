def perform_operation(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "%":
        return number1 % number2
    elif operator == "**":
        return number1 ** number2
    else:
        return "Invalid operator"

print('Available operators are: +, -, %, **')
number1 = int(input('Enter number1: '))
number2 = int(input('Enter number2: '))
operator = input('Enter operator: ')

result = perform_operation(number1, number2, operator)
print(result)