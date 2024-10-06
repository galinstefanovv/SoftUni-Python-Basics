import sys

data = input()
max_number = -sys.maxsize

while data != 'Stop':
    numbers = int(data)
    if numbers > max_number:
        max_number = numbers
    data = input()

print(max_number)