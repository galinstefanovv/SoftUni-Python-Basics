money = float(input())
year = int(input())
spend = 0
age = 18
for y in range(1800, year + 1):
    if y % 2 == 0:
        spend += 12000
    else:
        spend += 12000 + (50 * age)
    age += 1

if money >= spend:
    print(f'Yes! He will live a carefree life and will have {money - spend:.2f} dollars left.')
else:
    print(f'He will need {abs(money - spend):.2f} dollars to survive.')