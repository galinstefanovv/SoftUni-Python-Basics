season = input()
km = float(input())
price = 0
if km <= 5000:
    if season == 'Spring' or season == 'Autumn':
        price = km * 0.75 * 4
    elif season == 'Summer':
        price = km * 0.9 * 4
    elif season == 'Winter':
        price = km * 1.05 * 4
elif 5000 < km <= 10000:
    if season == 'Spring' or season == 'Autumn':
        price = km * 0.95 * 4
    elif season == 'Summer':
        price = km * 1.1 * 4
    elif season == 'Winter':
        price = km * 1.25 * 4
else:
    price = km * 1.45 * 4

price *= 0.9

print(f'{price:.2f}')
