fuel_type = input()
liters = float(input())
promo_card = input()
price = 0
if fuel_type == 'Gasoline':
    price = liters * 2.22
    if promo_card == 'Yes':
        price -= liters * 0.18
elif fuel_type == 'Diesel':
    price = liters * 2.33
    if promo_card == 'Yes':
        price -= liters * 0.12
elif fuel_type == 'Gas':
    price = liters * 0.93
    if promo_card == 'Yes':
        price -= liters * 0.08
else:
    print(f'Invalid data!')

if 20 <= liters <= 25:
    price *= 0.92
elif liters > 25:
    price *= 0.90

print(f'{price:.2f} lv.')
