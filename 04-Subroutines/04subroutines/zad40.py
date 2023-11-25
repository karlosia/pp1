def sum_of_repeated_digits(number):
    digit_count = {digit: str(number).count(digit) for digit in str(number) if digit.isdigit()}
    return sum(count for count in digit_count.values() if count > 1)

# Test cases
print(sum_of_repeated_digits(1027))     # Should print 0
print(sum_of_repeated_digits(230335))   # Should print 9
print(sum_of_repeated_digits(513553007)) # Should print 21