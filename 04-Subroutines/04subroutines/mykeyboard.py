def read_number(prompt):
        user_input = input(prompt)
        try:
            number = int(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return None

if __name__ == "__main__":
    num1=read_number('Enter the first number: ')
    num2=read_number('Enter the second number: ')

    if num1 is not None and num2 is not None:
        print(f'{num1} + {num2}={num1 + num2}')

