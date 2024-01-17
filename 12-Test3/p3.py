def f(uid):
    for element in uid:
        if uid.count(element)>1:
            return False
        else:
            return True
        
print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
print(f(["abc123","ann","abc123","a10"]))
print(f(["bob2","bob2"]))
print(f(["bob2","BOB2"]))        