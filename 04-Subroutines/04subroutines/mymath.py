def generate_number(prompt):
        import random
        print(prompt)
        number=random.randint(1,9)
        return number

random_number=generate_number('Number is: ')
print(f"Random number generated: {random_number}")