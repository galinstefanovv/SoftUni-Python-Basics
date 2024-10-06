import sys
city = input()
packet = input()
vip = input()
days = int(input())
price = 0
if days > 7:
    days = days - 1
if days < 1:
    print('Days must be positive number!')
elif city == "Bansko" or city == "Borovets":
    if packet == "withEquipment":
        price += 100
        if vip == "yes":
            price = price * 0.9
    elif packet == "noEquipment":
        price += 80
        if vip == "yes":
            price = price * 0.95
    else:
        print('Invalid input!')
        sys.exit()
    print(f'The price is {price * days:.2f}lv! Have a nice time!')
elif city == "Varna" or city == "Burgas":
    if packet == "withBreakfast":
        price += 130
        if vip == "yes":
            price = price * 0.88
    elif packet == "noBreakfast":
        price += 100
        if vip == "yes":
            price = price * 0.93
    else:
        print('Invalid input!')
        sys.exit()
    print(f'The price is {price * days:.2f}lv! Have a nice time!')
else:
    print('Invalid input!')
