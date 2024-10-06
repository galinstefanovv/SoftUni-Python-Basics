budget = float(input())
season = input()
car_type = ''
car_class = ''
price = budget
if budget <= 100:
    car_class = 'Economy class'
    if season == 'Summer':
        car_type = 'Cabrio'
        price *= 0.35
    elif season == 'Winter':
        car_type = 'Jeep'
        price *= 0.65
elif 100 < budget <= 500:
    car_class = 'Compact class'
    if season == 'Summer':
        car_type = 'Cabrio'
        price *= 0.45
    elif season == 'Winter':
        car_type = 'Jeep'
        price *= 0.8
else:
    car_class = 'Luxury class'
    car_type = 'Jeep'
    price *= 0.9

print(f'{car_class}\n'
      f'{car_type} - {price:.2f}')