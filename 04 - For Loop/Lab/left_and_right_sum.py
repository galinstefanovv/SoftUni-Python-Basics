number = int(input())
sum1 = 0
sum2 = 0

for left_sum in range(number):
    number1 = int(input())
    sum1 += number1
for right_sum in range(number):
    number1 = int(input())
    sum2 += number1

if sum1 == sum2:
    print(f'Yes, sum = {sum1}')
else:
    print(f'No, diff = {abs(sum1 - sum2)}')
