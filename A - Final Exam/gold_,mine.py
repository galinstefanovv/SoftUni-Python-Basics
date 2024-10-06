locations = int(input())
for i in range(1, locations + 1):
    gold_take = 0
    count = 0
    gold = float(input())
    days = int(input())
    for j in range (1, days + 1):
        gold_day = float(input())
        gold_take += gold_day
        count += 1
    total = gold_take / count
    if total >= gold:
        print(f'Good job! Average gold per day: {total:.2f}.')
    else:
        print(f'You need {abs(total - gold):.2f} gold.')