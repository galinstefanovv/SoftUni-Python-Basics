budget = float(input())
statist = int(input())
price_per_outfit = float(input())

decor = budget * 0.1

if statist > 150:
    price_per_outfit -= price_per_outfit * 0.1

total_price = statist * price_per_outfit + decor

diff = budget - total_price

if diff < 0:
    print(f'Not enough money!\n'
          f'Wingard needs {abs(diff):.2f} leva more.')
else:
    print(f'Action!\n'
          f'Wingard starts filming with {abs(diff):.2f} leva left.')
