def f(n):
    fib_sequence = [0, 1]

    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[-1]

n = int(input('Enter n: '))
print(f(n))
   