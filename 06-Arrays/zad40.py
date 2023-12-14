def display_array_formatted(array):
    
    if len(array) != 8:
        print("Error: The array must contain exactly 8 elements.")
        return

    
    print("-----------------------------------------")
    for num in array:
        print(f"|{num:4}", end="")
    print("|")
    print("-----------------------------------------")


array_of_numbers = [1, 23, 5, 382, 1, 17, 4, 906]
display_array_formatted(array_of_numbers)
