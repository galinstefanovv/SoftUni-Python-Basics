months = int(input())
electricity = 0
water = 0
internet = 0
other = 0
average = 0
for i in range(months):
    bill = float(input())
    electricity += bill
    water += 20
    internet += 15
    total_other = bill + 20 + 15
    other += total_other + total_other * 0.2

bill = electricity + water + internet + other

print(f'Electricity: {electricity:.2f} lv\n'
      f'Water: {water:.2f} lv\n'
      f'Internet: {internet:.2f} lv\n'
      f'Other: {other:.2f} lv\n'
      f'Average: {bill / months:.2f} lv')
