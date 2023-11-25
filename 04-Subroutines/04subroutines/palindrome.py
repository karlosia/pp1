def f(palindrome):
    cleaned_expression=''.join(char.lower() for char in palindrome)
    return cleaned_expression==cleaned_expression[::-1]
palindrome='radar'
print(f(palindrome)) 