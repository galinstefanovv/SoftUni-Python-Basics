from math import ceil
guests = int(input())
budget = int(input())


bread_count = ceil(guests / 3)
egg_count = guests * 2

bread_price = bread_count * 4
egg_price = egg_count * 0.45

total = bread_price + egg_price

if total <= budget:
    print(f'Lyubo bought {bread_count} Easter bread and {egg_count} eggs.')
    print(f'He has {abs(total - budget):.2f} lv. left.')
else:
    print(f"Lyubo doesn't have enough money.")
    print(f'He needs {abs(total - budget):.2f} lv. more.')