with open('File-OK11O.txt','r') as file1:
    content=file1.read()

with open('Copied.txt', 'w') as file2:
    file2.write(content)    

