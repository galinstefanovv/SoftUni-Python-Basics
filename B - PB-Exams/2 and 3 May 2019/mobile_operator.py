promise = input()
type = input()
internet = input()
months = int(input())
price = 0
if promise == "one":
    if type == "Small":
        price += 9.98
    elif type == "Middle":
        price += 18.99
    elif type == "Large":
        price+= 25.98
    elif type == "ExtraLarge":
        price += 35.99
elif promise == "two":
    if type == "Small":
        price += 8.58
    elif type == "Middle":
        price += 17.09
    elif type == "Large":
        price+= 23.59
    elif type == "ExtraLarge":
        price += 31.79
if internet == "yes":
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    else:
        price += 3.85
total = price * months
if promise == "two":
    total = total - (total * 0.0375)
print(f'{total:.2f} lv.')


