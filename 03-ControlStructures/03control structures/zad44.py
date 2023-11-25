sum_of_numbers=0
count_of_numbers=0

while True:
    user_input=float(input("Enter number: "))
    if user_input==0:
        break
    sum_of_numbers=sum_of_numbers+user_input
    count_of_numbers+=1

mean=sum_of_numbers/count_of_numbers    

print(f"RESULT: Quantity={count_of_numbers}, Sum={sum_of_numbers}, Mean={mean}")         
         

