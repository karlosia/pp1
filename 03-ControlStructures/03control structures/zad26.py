car_speed=int(input("Enter car speed: "))
speed_limit_min=40
speed_limit_max=140


if car_speed>140:
    print(f'Car speed has been exceeded')
elif car_speed<40:
    print(f'Warning: invalid car speed!!')
else:
    print(f'Correct speed')         