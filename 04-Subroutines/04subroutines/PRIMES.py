def is_prime(num):
    return num>1 and all(num%i!=0 for i in range(2, int(num**0.5)+1))


def f(n):
    prime_numbers=[]
    num=2
    while len(prime_numbers)<n:
        if is_prime:
            prime_numbers.append(num)
        num=num+1
    return prime_numbers[-1]           
