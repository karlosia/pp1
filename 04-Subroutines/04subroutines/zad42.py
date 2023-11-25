def f(number1,number2,number3):
    maxnumbers=max(number1,number2,number3)
    minnumbers=min(number1,number2,number3)
    result=maxnumbers-minnumbers
    return result

print(f(7,4,9))  