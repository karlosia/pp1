real_pin="0805"
max_attempts=3



for attempts in range(max_attempts):
        pin=input("Enter the PIN code: ")
        if pin==real_pin:
            print("Correct")
            break
        else:
            print("Incorrect")
if pin!=real_pin:
    print("Sorry, your payment card has been blocked.")            


    
