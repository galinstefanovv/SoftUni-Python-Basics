from math import pi
type = input()
total = 0
if type == 'square':
    a = float(input())
    total = a**2
elif type == 'rectangle':
    a = float(input())
    b = float(input())
    total = a * b
elif type == 'circle':
    r = float(input())
    total = pi * r**2
elif type == 'triangle':
    a = float(input())
    b = float(input())
    total = (a * b) / 2

print(f'{total:.3f}')