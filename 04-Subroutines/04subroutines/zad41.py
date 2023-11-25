def nth_prime(n):
    primes=[]
    num=2

    while len(primes)<n:
        is_prime=all(num%prime!=0 for prime in primes)
        if is_prime:
            primes.append(num)
        num=num+1
    return primes[-1]    

print(nth_prime(1))  # Should print 2
print(nth_prime(5))    