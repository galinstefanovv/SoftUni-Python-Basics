annual_tax = int(input())

sneakers = annual_tax - annual_tax * 0.4
sport_outfit = sneakers - sneakers * 0.2
ball = sport_outfit * 0.25
accessories = ball * 0.2

total_sum = annual_tax + sneakers + sport_outfit + ball + accessories
print(total_sum)