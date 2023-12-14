

sth=[f'{i**1},{i**2},{i**3}' for i in range(1,11)]

with open('powers.txt','w') as file:
    for element in sth:
        file.write(element+'\n')