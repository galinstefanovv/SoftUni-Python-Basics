chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()
price = 0

if season == 'Spring' or season == 'Summer':
    price = (chrysanthemums * 2) + (roses * 4.1) + (tulips * 2.5)
    if season == 'Spring' and tulips > 7:
        price *= 0.95
elif season == 'Autumn' or season == 'Winter':
    price = (chrysanthemums * 3.75) + (roses * 4.5) + (tulips * 4.15)
    if season == 'Winter' and roses >= 10:
        price *= 0.90

if roses + tulips + chrysanthemums > 20:
    price *= 0.8


if holiday == 'Y':
    price += price * 0.15

print(f'{price + 2:.2f}')
