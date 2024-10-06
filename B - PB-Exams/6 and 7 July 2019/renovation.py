from math import ceil
size = int(input()) * int(input())
percentage = int(input()) / 100
input_line = input()
total_m = size * 4
without_w = total_m - (total_m * percentage)
sum = 0
while True:
    if input_line == "Tired!":
        print(f'{ceil(abs(sum - without_w))} quadratic m left.')
        break
    liters = int(input_line)
    sum += liters
    if sum > without_w:
        print(f'All walls are painted and you have {ceil(abs(sum - without_w))} l paint left!')
        break
    if sum == without_w:
        print(f'All walls are painted! Great job, Pesho!')
        break
    input_line = input()