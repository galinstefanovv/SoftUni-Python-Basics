import math
x = int(input())
y = float(input())
z = int(input())
employees = int(input())
vine = (x * y) * 0.4
grapes = vine / 2.5

total = abs(grapes - z)
liters_per_person = total / employees

if grapes >= z:
    print(f'Good harvest this year! Total wine: {math.floor(grapes)} liters.')
    print(f'{math.ceil(total)} liters left -> {math.ceil(liters_per_person)} liters per person.')
else:
    print(f'It will be a tough winter! More {math.floor(total)} liters wine needed.')