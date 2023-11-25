def number_of_negative_even_numbers(x,y):
    return sum(1 for num in range(x,y) if num<0 and num%2==0)

x=int(input('Enter x: '))
y=int(input('Enter y: '))

result=number_of_negative_even_numbers(x, y)
print(result)
