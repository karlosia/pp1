import random

random_numbers=[random.randint(100,999) for _ in range(50)]
with open('random.txt','w') as file:
    for number in random_numbers:
        file.write(str(number)+'\n')