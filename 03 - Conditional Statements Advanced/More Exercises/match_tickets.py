budget = float(input())
category = input()
people = int(input())
transport = budget
ticket_price = 0
if category == 'VIP':
    ticket_price = 499.99 * people
else:
    ticket_price = 249.99 * people

if 1 <= people <= 4:
    transport *= 0.75
elif 5 <= people <= 9:
    transport *= 0.6
elif 10 <= people <= 24:
    transport *= 0.5
elif 25 <= people <= 49:
    transport *= 0.4
else:
    transport *= 0.25


money_left = budget - transport - ticket_price

if money_left < 0:
    print(f'Not enough money! You need {abs(money_left):.2f} leva.')
else:
    print(f'Yes! You have {money_left:.2f} leva left.')

