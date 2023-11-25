def minimum_coins(amount_to_pay):
    coins_count=0

    coins_count=coins_count+amount_to_pay//5
    amount_to_pay%=5

    coins_count=coins_count+amount_to_pay//2
    amount_to_pay%=2

    coins_count=coins_count+amount_to_pay

    return coins_count


amount_to_pay=int(input('Enter your amount to pay: '))
print(minimum_coins(amount_to_pay))  
