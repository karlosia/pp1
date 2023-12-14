def f(arr):
    valid_username=0
    for username in arr:
        if 4<len(username)<12 and '_' in username and any(char.isdigit() for char in username) and any(char.islower() for char in username):
            valid_username+=1
    return valid_username

print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))        