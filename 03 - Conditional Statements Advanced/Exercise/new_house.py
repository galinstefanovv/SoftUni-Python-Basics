flowers_type = input()
flowers_qty = int(input())
budget = int(input())
price = 0


if flowers_type == 'Roses':
    price = flowers_qty * 5
    if flowers_qty > 80:
        price -= price * 0.1
elif flowers_type == 'Dahlias':
    price = flowers_qty * 3.8
    if flowers_qty > 90:
        price -= price * 0.15
elif flowers_type == 'Tulips':
    price = flowers_qty * 2.8
    if flowers_qty > 80:
        price -= price * 0.15
elif flowers_type == 'Narcissus':
    price = flowers_qty * 3
    if flowers_qty < 120:
        price += price * 0.15
elif flowers_type == 'Gladiolus':
    price = flowers_qty * 2.5
    if flowers_qty < 80:
        price += price * 0.2

diff = abs(budget - price)

if budget >= price:
    print(f'Hey, you have a great garden with {flowers_qty} {flowers_type} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')
