def is_negative(n1,n2,n3):
    if n1<0 or n2<0 or n3<0:
        return True
    else:
        return False
    
n1=int(input('Enter n1: '))
n2=int(input('Enter n2: '))
n3=int(input('Enter n3: '))    

result=is_negative(n1,n2,n3)
print(result)