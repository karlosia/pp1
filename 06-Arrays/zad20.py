arr=[34,7,19,4,21,8]

evens=0
index=0

def is_even(i):
    if i%2==0:
        return True
    else:
        return False        
    
while len(arr)>index:
    if is_even(arr[index]):
        evens=evens+1
    index=index+1    
        
print(evens)        
        
        