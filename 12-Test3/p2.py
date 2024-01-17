def f(x,y,digit):
    counter=0
    for i in range(x,y+1):
        a=str(i).count(str(digit))
        counter+=a
    return counter

print(f(10,15,1))    
print(f(28,32,2))
print(f(100,105,6))
