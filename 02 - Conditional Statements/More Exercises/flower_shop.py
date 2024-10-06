import math

magnolias = int(input()) * 3.25
hyacinths = int(input()) * 4
roses = int(input()) * 3.5
cacti = int(input()) * 8
gift_price = float(input())

total = (magnolias + hyacinths + roses + cacti) * 0.95
diff = abs(gift_price - total)
if total >= gift_price:
    print(f'She is left with {math.floor(diff)} leva.')
else:
    print(f'She will have to borrow {math.ceil(diff)} leva.')