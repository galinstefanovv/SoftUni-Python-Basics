budget = float(input())
needed_liters = float(input())
day = input()

gas = needed_liters * 2.10
total = gas + 100
if day == "Saturday":
    total = total * 0.9
elif day == "Sunday":
    total = total * 0.8

if total <= budget:
    print(f'Safari time! Money left: {abs(total - budget):.2f} lv.')
else:
    print(f'Not enough money! Money needed: {abs(total - budget):.2f} lv.')