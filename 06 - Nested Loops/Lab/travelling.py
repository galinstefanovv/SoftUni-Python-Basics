destination = input()

while destination != 'End':
    min_budget = float(input())
    saved_money = 0
    while saved_money < min_budget:
        save = float(input())
        saved_money += save
    print(f'Going to {destination}!')
    destination = input()