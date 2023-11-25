def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


N = int(input("Enter the value of N: "))


prime_numbers = []
number = 2 

while len(prime_numbers) < N:
    if is_prime(number):
        prime_numbers.append(number)
    number += 1


print(f"Prime numbers: {' '.join(map(str, prime_numbers))}")
