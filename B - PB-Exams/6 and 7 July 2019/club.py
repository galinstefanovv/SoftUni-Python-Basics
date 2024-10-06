money = float(input())
input_line = input()
sum = 0
total = 0
acquired = False
while input_line != "Party!":
    number = int(input())
    sum = len(input_line) * number
    if sum % 2 != 0:
        sum *= 0.75
    total += sum
    if total >= money:
        acquired = True
        break
    input_line = input()
if acquired:
    print(f'Target acquired.')
    print(f'Club income - {abs(total):.2f} leva.')
else:
    print(f'We need {abs(total-money):.2f} leva more.')
    print(f'Club income - {abs(total):.2f} leva.')