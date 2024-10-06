import sys
number = int(input())
max_number = -sys.maxsize
sums = 0
total_sum = 0
for numbers in range(0, number):
    number = int(input())
    sums += number
    if number > max_number:
        max_number = number
    total_sum = sums - max_number
if total_sum == max_number:
    print("Yes")
    print(f'Sum = {total_sum}')
else:
    print("No")
    print(f'Diff = {abs(max_number - total_sum)}')