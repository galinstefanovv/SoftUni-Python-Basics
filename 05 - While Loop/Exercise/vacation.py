req_money = float(input())
av_money = float(input())
spend = 0
days = 0
no_save = False
while True:
    action = input()
    amount = float(input())
    days += 1
    if action == "spend":
        av_money = av_money - amount
        if av_money < 0:
            av_money = 0
        spend += 1
        if spend == 5:
            no_save = True
            break
    elif action == "save":
        av_money = av_money + amount
        spend = 0
    if av_money >= req_money:
        break
if no_save:
    print(f"You can't save the money.")
    print(f'{days}')
else:
    print(f'You saved the money for {days} days.')