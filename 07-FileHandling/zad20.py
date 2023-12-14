with open('MeatAndFish.txt','r') as file1:
    content=file1.read()
with open('GrainsAndBread.txt','r') as file2:
    content+=file2.read()

with open('allproducts.txt','w') as result:
    result.write(content)        