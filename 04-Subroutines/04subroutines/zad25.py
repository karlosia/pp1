greater_than= lambda x,y: True if x>y else False
x=int(input('Enter x: '))
y=int(input('Enter y: '))
pair1_result = greater_than(x, y)
pair2_result = greater_than(19, 23)

print(f"For the pair ({x}, {y}): {pair1_result}")
print(f"For the pair (19, 23): {pair2_result}")