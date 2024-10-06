from math import ceil
people = int(input())
tax = float(input())
lounge = float(input())
umbrella = float(input())

lounge_taxes = ceil(people * 0.75) * lounge
umbrella_taxes = ceil(people / 2) * umbrella
tax_total = people * tax

total = lounge_taxes + umbrella_taxes + tax_total

print(f'{total:.2f} lv.')
