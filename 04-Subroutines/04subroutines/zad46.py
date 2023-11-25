def sum_numbers(x, y):
    result = 0
    for number in range(x, y+1):
        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:
            result += number
    return result


print(sum_numbers(1, 20))
print(sum_numbers(10, 30))  