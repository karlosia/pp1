def f(p):
    if len(p)<6:
        return False
    
    different_characters=set(p)

    if len(different_characters)>=6:
        return True
    
p="123456"
result=f(p)
print(result)  
