def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n - 1)

# Przykład użycia
result = sum_recursive(10)
print(result)