budget = float(input())
input_line = input()
count = 0
sum = 0
nomoney = False
while input_line != "Stop":
    price = float(input())
    count += 1
    if count % 3 == 0:
        price = price / 2
    sum += price
    if sum > budget:
        nomoney = True
        break
    input_line = input()
if nomoney:
    print(f"You don't have enough money!")
    print(f'You need {abs(budget - sum):.2f} leva!')
else:
    print(f'You bought {count} products for {sum:.2f} leva.')