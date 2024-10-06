days = int(input()) - 1
room = input()
review = input()
price = 0

if room == 'room for one person':
    price = 18 * days
elif room == 'apartment':
    price = 25 * days
    if days < 10:
        price *= 0.7
    elif 10 <= days <= 15:
        price *= 0.65
    elif days > 15:
        price *= 0.5
elif room == 'president apartment':
    price = 35 * days
    if days < 10:
        price *= 0.9
    elif 10 <= days <= 15:
        price *= 0.85
    elif days > 15:
        price *= 0.8

if review == 'positive':
    price += price * 0.25
else:
    price *= 0.9

print(f'{price:.2f}')