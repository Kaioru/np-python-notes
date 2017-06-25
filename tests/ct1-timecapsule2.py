import math

radius = float(input('Radius of the sphere: '))
height = float(input('Height of the column: '))
width = float(input('Width of the cube: : '))

radiusSA = 4 * math.pi * radius ** 2
columnSA = 2 * math.pi * (radius / 2) * height + 2 * math.pi * (radius / 2) ** 2
cubeSA = 6 * width ** 2

totalSA = radiusSA + columnSA + cubeSA

print('The total surface area of the Time Capsule is %.2f' % totalSA)
