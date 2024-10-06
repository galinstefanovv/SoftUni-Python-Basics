from math import floor
import sys

input_line = input()
max_num = -sys.maxsize
word = ""
while input_line != "End of words":
    sum = 0
    for i in range(0, len(input_line)):
        sum += ord(input_line[i])

    if input_line[0] == "a" or input_line[0] == "e" or input_line[0] == "i" or input_line[0] == "o" or \
            input_line[0] == "u" or input_line[0] == "y" or input_line[0] == "A" or input_line[0] == "E" or \
            input_line[0] == "I" or input_line[0] == "O" or input_line[0] == "U" or input_line[0] == "Y":
        sum = sum * len(input_line)
    else:
        sum = floor(sum / len(input_line))
    if sum > max_num:
        max_num = sum
        word = input_line
    input_line = input()
print(f'The most powerful word is {word} - {max_num}')
