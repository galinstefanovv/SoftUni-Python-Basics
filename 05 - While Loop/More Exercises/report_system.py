needed_sum = int(input())
input_line = input()
collected_money = 0
cash = 0
cash_count = 0
card = 0
card_count = 0
count = 0
failed = False
while True:
    if input_line == 'End':
        failed = True
        print(f'Failed to collect required money for charity.')
        break
    collect = int(input_line)
    count += 1
    if count % 2 == 0:
        if collect < 10:
            print(f'Error in transaction!')
        else:
            card += 1
            card_count += collect
            collected_money += collect
            print(f'Product sold!')
    else:
        if collect > 100:
            print(f'Error in transaction!')
        else:
            cash += 1
            cash_count += collect
            collected_money += collect
            print(f'Product sold!')
    if needed_sum <= collected_money:
        break
    input_line = input()

if not failed:
    print(f'Average CS: {cash_count / cash:.2f}\n'
          f'Average CC: {card_count / card:.2f}')
