budget = int(input())
season = input()
fishermen = int(input())
price = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
else:
    price = 2600

if fishermen <= 6:
    price -= price * 0.1
elif 7 <= fishermen <= 11:
    price -= price * 0.15
else:
    price -= price * 0.25

if fishermen % 2 == 0 and not season == 'Autumn':
    price -= price * 0.05

diff = abs(budget - price)

if budget >= price:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')