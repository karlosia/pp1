jacket=40
underwear=70
shoes=20
rinse=15
spin=9

total_washing_time = 0

washing_product = int(input("Enter washing product (1 for jacket, 2 for underwear, 3 for shoes): "))
rinse_option = bool(input("Do you want an additional rinse? Enter true or false: ").lower() == 'true')
spin_option = bool(input("Do you want an additional spin? Enter true or false: ").lower() == 'true')




if washing_product==1:
    total_washing_time+=jacket
elif washing_product==2:
    total_washing_time+=underwear
elif washing_product==3: 
    total_washing_time+=shoes
else:
    print("INVALID")

if rinse_option:
    total_washing_time+=rinse

if spin_option:
    total_washing_time+=spin

print(f'Total washing time is {total_washing_time}')              

