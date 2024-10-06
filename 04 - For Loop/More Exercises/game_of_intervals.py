turns = int(input())
points = 0
first = 0
second = 0
third = 0
fourth = 0
fifth = 0
invalid = 0
for turn in range(turns):
    number = int(input())
    if 0 <= number <= 9:
        points += number * 0.2
        first += 1
    elif 10 <= number <= 19:
        points += number * 0.3
        second += 1
    elif 20 <= number <= 29:
        points += number * 0.4
        third += 1
    elif 30 <= number <= 39:
        points += 50
        fourth += 1
    elif 40 <= number <= 50:
        points += 100
        fifth += 1
    else:
        points /= 2
        invalid += 1

print(f'{points:.2f}\n'
      f'From 0 to 9: {first / turns * 100:.2f}%\n'
      f'From 10 to 19: {second / turns * 100:.2f}%\n'
      f'From 20 to 29: {third / turns * 100:.2f}%\n'
      f'From 30 to 39: {fourth / turns * 100:.2f}%\n'
      f'From 40 to 50: {fifth / turns * 100:.2f}%\n'
      f'Invalid numbers: {invalid / turns * 100:.2f}%')