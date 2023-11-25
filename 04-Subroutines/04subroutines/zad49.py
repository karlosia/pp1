def max_dice_sequence(dice):
    if not dice:
        return 0

    max_count = 1
    current_count = 1

    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            current_count += 1
        else:
            current_count = 1

        max_count = max(max_count, current_count)

    return max_count


print(max_dice_sequence("5233165554211")) 
print(max_dice_sequence("2133"))    