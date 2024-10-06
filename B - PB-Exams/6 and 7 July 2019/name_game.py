import sys
name = input()
max_num = -sys.maxsize
player = ""
while True:
    length = len(name)
    points = 0
    if name == "Stop":
        print(f'The winner is {player} with {max_num} points!')
        break
    for i in range(0, length):
        number = int(input())
        text = name[i]
        if number == ord(text):
            points += 10
        else:
            points += 2
        if points >= max_num:
            max_num = points
            player = name

    name = input()

