from math import floor, ceil
days = int(input())
food_left = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input()) / 1000

total_food = (dog_food + cat_food + turtle_food) * days
diff = abs(food_left - total_food)
if total_food > food_left:
    print(f'{ceil(diff)} more kilos of food are needed.')
else:
    print(f'{floor(diff)} kilos of food left.')