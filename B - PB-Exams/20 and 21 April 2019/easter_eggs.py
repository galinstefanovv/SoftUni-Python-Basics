import sys
eggs = int(input())
red = 0
orange = 0
blue = 0
green = 0
total = 0
max = -sys.maxsize
word = ""
for i in range(1, eggs + 1):
    color = input()

    if color == "red":
        red += 1
        if red > max:
            max = red
            word = "red"
    elif color == "orange":
        orange += 1
        if orange > max:
            max = orange
            word = "orange"
    elif color == "blue":
        blue += 1
        if blue > max:
            max = blue
            word = "blue"
    elif color == "green":
        green += 1
        if green > max:
            max = green
            word = "green"
print(f'Red eggs: {red}')
print(f'Orange eggs: {orange}')
print(f'Blue eggs: {blue}')
print(f'Green eggs: {green}')
print(f'Max eggs: {max} -> {word}')


