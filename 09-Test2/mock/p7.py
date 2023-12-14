def f(arr):
    number_of_valid_usernames=0
    for element in arr:
        if 4<=len(element)<=12 and '_' in element and any(char.isdigit() for char in element) and any(char.islower() for char in element):
                number_of_valid_usernames+=1
    return number_of_valid_usernames            
            
    


print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))

