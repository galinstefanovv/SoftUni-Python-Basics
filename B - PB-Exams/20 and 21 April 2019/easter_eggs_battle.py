first = int(input())
second = int(input())
one = False
two = False
input_line = input()
while input_line != "End":
    if input_line == "one":
        second -= 1
    elif input_line == "two":
        first -= 1
    if first <= 0:
        one = True
        break
    if second <= 0:
        two = True
        break
    input_line = input()
if one:
    print(f'Player one is out of eggs. Player two has {second} eggs left.')
elif two:
    print(f'Player two is out of eggs. Player one has {first} eggs left.')
else:
    print(f'Player one has {first} eggs left.')
    print(f'Player two has {second} eggs left.')