with open('techtext.txt','r') as file1:
    content=file1.readlines()[1:6]

with open('techtextcopy.txt','w') as file2:
    file2.writelines(content)