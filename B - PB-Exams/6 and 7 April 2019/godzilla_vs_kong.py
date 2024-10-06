budget = float(input())
statist = int(input())
money = float(input())
decor = budget * 0.1
if statist > 150:
    money = money - (money * 0.1)
total = decor + money * statist
diff = abs(total - budget)
if total > budget:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')