# Kirjuta programm, mis küsib kasutajalt raadiuse ja arvutab ringi pindala ja ümbermõõdu. (math.pi)
#veel võimalusi importimiseks from math import pi - impordin ainult ühe asja


import math

radius = int(input('Kirjuta ringi raadius: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2

print('Ümbermõõt on', round(perimeter, 4))
print('Pindala on', round(area, 4))
