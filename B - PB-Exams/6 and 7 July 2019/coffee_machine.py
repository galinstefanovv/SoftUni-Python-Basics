drink = input()
sugar = input()
amount = int(input())
sum = 0
if drink == "Espresso":
    if sugar == "Without":
        sum = 0.9 * 0.65
    elif sugar == "Normal":
        sum = 1
    elif sugar == "Extra":
        sum = 1.20
    if amount >= 5:
        sum = sum * 0.75
elif drink == "Cappuccino":
    if sugar == "Without":
        sum = 1 * 0.65
    elif sugar == "Normal":
        sum = 1.20
    elif sugar == "Extra":
        sum = 1.60
elif drink == "Tea":
    if sugar == "Without":
        sum = 0.50 * 0.65
    elif sugar == "Normal":
        sum = 0.60
    elif sugar == "Extra":
        sum = 0.70
total = sum * amount
if total > 15:
    total = total * 0.8

print(f'You bought {amount} cups of {drink} for {total:.2f} lv.')
