coordinates=input("Enter the plane coordinates (point P): ")

x,y=map(int, coordinates.split(','))

print(f'x={x}')
print(f'y={y}')

if x == 0 and y == 0:
    print(f'Point P is located in the position (0,0) of the coordinate system.')
elif x > 0 and y > 0:
    print(f'Point P({x},{y}) is in the first quadrant of the coordinate system.')
elif x > 0 and y < 0:
    print(f'Point P({x},{y}) is in the second quadrant of the coordinate system.')
elif x < 0 and y < 0:
    print(f'Point P({x},{y}) is in the third quadrant of the coordinate system.')
elif x<0 and y>0:
    print(f'Point P({x},{y}) is in the fourth quadrant of the coordinate system.')
elif x==0 and y>0 or y<0:
    print(f'Point P({x},{y}) is on the OY  of the coordinate system.')
else:
    print(f'Point P({x},{y}) is on the OX of the coordinate system.') 