import sys

data = input()
min_number = sys.maxsize

while data != 'Stop':
    numbers = int(data)
    if numbers < min_number:
        min_number = numbers
    data = input()

print(min_number)