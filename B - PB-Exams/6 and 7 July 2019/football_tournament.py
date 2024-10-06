team = input()
play = int(input())
points = 0
w = 0
d = 0
l = 0
zero = False
if play == 0:
    zero = True
else:
    for i in range(0, play):
        end = input()
        if end == "W":
            points += 3
            w += 1
        elif end == "D":
            points += 1
            d += 1
        elif end == "L":
            points += 0
            l += 1
if zero:
    print(f"{team} hasn't played any games during this season.")
else:
    print(f'{team} has won {points} points during this season.')
    print(f'Total stats:')
    print(f'## W: {w}')
    print(f'## D: {d}')
    print(f'## L: {l}')
    print(f'Win rate: {(w / play) * 100:.2f}%')

