from math import ceil, floor
price = float(input())
qty_rocket = int(input())
qty_shoes = int(input())
shoes_price = price / 6
sum = (qty_rocket * price) + (qty_shoes * shoes_price)
other = sum * 0.2
total_price = sum + other
print(f'Price to be paid by Djokovic {floor(total_price / 8)}')
print(f'Price to be paid by sponsors {ceil((total_price * 7) / 8)}')