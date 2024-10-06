n = int(input())
sum_even = 0
sum_odd = 0

for i in range(n):
    numbers = int(input())
    if i % 2 == 0:
        sum_even += numbers
    else:
        sum_odd += numbers

if sum_even == sum_odd:
    print(f'Yes\n'
          f'Sum = {sum_even}')
else:
    print(f'No\n'
          f'Diff = {abs(sum_even - sum_odd)}')