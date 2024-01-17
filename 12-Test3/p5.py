class C:
    def __init__(self,initial_value):
        self.counter=initial_value

    def m1(self):
        return self.counter
    def m2(self):
        self.counter+=1
    def m3(self):
        self.counter-=1
    def m4(self,n):
        self.counter+=n
    def ___str___(self):
        return str(self.counter)
    
c=C(5)

print(c.m1())    # Output: 5
c.m2()
print(c.m1())    # Output: 6
c.m4(-8)
print(c.m1())    # Output: -2
c.m3()
print(c.m1())    # Output: -3
c.m4(10)
print(c.m1())    # Output: 7
print(c.__str__())  # Output: "7"

    



