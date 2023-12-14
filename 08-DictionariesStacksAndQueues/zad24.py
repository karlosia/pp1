from stack import push,pop,empty,display

def decimal_to_binary(number):
    if number<0:
        print('Please enter a natural number.')
        return
    
    while number>0:
        remainder=number%2
        push(remainder)
        number//=2

    print('Binary representation: ')
    while not empty():
        print(pop(),end="")
    print()    

decimal_to_binary(18)    