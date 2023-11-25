def f(product_code):
    if len(product_code)!=4:
        return False
    else:
        numbers=[int(digit) for digit in product_code]
        if sum(numbers[0],numbers[1],numbers[2])%7==numbers[3]:
            return True
        else:
            return False
        
product_code="1082"         
result=f(product_code)    