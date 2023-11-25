personal_data="Mr. John May, born on 1998-02-16"

name=personal_data[4:8]
surname=personal_data[9:12]
initials=personal_data[4:5]+personal_data[9:10]
born=personal_data[22:33]

print(f'Name: {name}')
print(f'Surname: {surname}')
print(f'Initials: {initials}')
print(f'Born: {born}')     