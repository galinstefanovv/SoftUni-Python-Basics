stadium_capacity = int(input())
fans = int(input())
a = 0
b = 0
v = 0
g = 0
for fan in range(fans):
    sector = input()
    if sector == 'A':
        a += 1
    elif sector == 'B':
        b += 1
    elif sector == 'V':
        v += 1
    elif sector == 'G':
        g += 1

print(f'{a / fans * 100:.2f}%\n'
      f'{b / fans * 100:.2f}%\n'
      f'{v / fans * 100:.2f}%\n'
      f'{g / fans * 100:.2f}%\n'
      f'{fans / stadium_capacity * 100:.2f}%')