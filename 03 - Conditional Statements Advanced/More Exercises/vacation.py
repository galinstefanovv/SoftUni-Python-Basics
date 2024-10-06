budget = float(input())
season = input()
place = ''
location = ''
price = budget
if budget <= 1000:
    place = 'Camp'
    if season == 'Summer':
        price *= 0.65
    elif season == 'Winter':
        price *= 0.45
elif 1000 < budget <= 3000:
    place = 'Hut'
    if season == 'Summer':
        price *= 0.80
    elif season == 'Winter':
        price *= 0.60
else:
    place = 'Hotel'
    price *= 0.9

if season == 'Summer':
    location = 'Alaska'
else:
    location = 'Morocco'

print(f'{location} - {place} - {price:.2f}')