first = input()
second = input()

input_line = input()
points_first = 0
points_second = 0
win = False
while input_line != "End of game":
    first_player = int(input_line)
    second_player = int(input())
    if first_player == second_player:
        print(f'Number wars!')
        first_new = int(input())
        second_new = int(input())
        if first_new > second_new:
            print(f'{first} is winner with {points_first} points')
        elif second_new > first_new:
            print(f'{second} is winner with {points_second} points')
        win = True
        break
    elif first_player > second_player:
        points_first += abs(first_player - second_player)
    else:
        points_second += abs(first_player - second_player)
    input_line = input()
if not win:
    print(f'{first} has {points_first} points')
    print(f'{second} has {points_second} points')