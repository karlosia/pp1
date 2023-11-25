def numbers(n):
    return ' '.join(map(str,range (1,n+1)))

print(f'Numbers <1,15>: {numbers(15)}')
print(f'Numbers <1,7>: {numbers(7)}')