days = int(input())
hours = int(input())
tax = 0
for i in range(1, days + 1):
    tax_for_day = 0

    for j in range(1, hours + 1):
        if i % 2 == 0 and j % 2 != 0:
            tax += 2.5
            tax_for_day += 2.5
        elif i % 2 != 0 and j % 2 == 0:
            tax += 1.25
            tax_for_day += 1.25
        else:
            tax += 1
            tax_for_day += 1

    print(f'Day: {i} - {tax_for_day:.2f} leva')
print(f'Total: {tax:.2f} leva')
