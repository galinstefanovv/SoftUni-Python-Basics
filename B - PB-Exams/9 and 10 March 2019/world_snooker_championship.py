stage = input()
type = input()
qty = int(input())
photo = input()
price = 0
photo_p = 40 * qty
if stage == "Quarter final":
    if type == "Standard":
        price += 55.50
    elif type == "Premium":
        price += 105.20
    elif type == "VIP":
        price += 118.90
elif stage == "Semi final":
    if type == "Standard":
        price += 75.88
    elif type == "Premium":
        price += 125.22
    elif type == "VIP":
        price += 300.40
elif stage == "Final":
    if type == "Standard":
        price += 110.10
    elif type == "Premium":
        price += 160.66
    elif type == "VIP":
        price += 400
total = price * qty

if total > 4000:
    total *= 0.75
    photo_p = 0
elif total > 2500:
    total *= 0.9
if photo == "Y":
    total += photo_p
print(f'{total:.2f}')