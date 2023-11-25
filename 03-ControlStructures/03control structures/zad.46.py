def display_lottery_coupon():
    numbers=list(range(1,50))

    for i in range(7):
        for j in range(7):
            index=i+j*7
            print(f'{numbers[index]:2}', end=' ')
        print()
display_lottery_coupon()        