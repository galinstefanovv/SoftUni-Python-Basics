eggs = int(input())

input_line = input()
over = False
total = 0
while input_line != "Close":
    amount = int(input())
    if input_line == "Buy":
        if amount > eggs:
            over = True
            break
        total += amount
        eggs -= amount
    elif input_line == "Fill":
        eggs += amount
    input_line = input()

if over:
    print(f'Not enough eggs in store!')
    print(f'You can buy only {eggs}.')
else:
    print(f'Store is closed!')
    print(f'{total} eggs sold.')