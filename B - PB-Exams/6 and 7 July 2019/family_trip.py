budget = float(input())
nights = int(input())
price = float(input())
percentage = int(input()) / 100

if nights > 7:
    price *= 0.95
additional = budget * percentage
sum = (nights * price) + additional
diff = abs(budget - sum)
if budget >= sum:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{diff:.2f} leva needed.')