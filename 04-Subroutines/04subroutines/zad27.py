def card_number(number):
    number_str=str(number)
    
    
    if len(number_str)==16:
        cyfry=list(number_str)
        cyfry[3:13]=['*' for _ in range(10)]
        modified_number_str=''.join(cyfry)
        return modified_number_str
    else:
        return "Invalid card number length"
    
if __name__=='__main__':
    number=int(input('Enter your card number: '))
    result=card_number(number)
    print(result)