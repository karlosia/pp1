def f(a,b):
    if a>b:
        subtraction=a-b
        return str(f'{a}-{b}={subtraction}')
    else:
        summation=a+b
        return str(f'{a}+{b}={summation}')
    
a=20
b=8

result=(f(a,b))
print(result)