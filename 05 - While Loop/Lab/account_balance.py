input_field = input()
sums = 0

while True:
    if input_field == 'NoMoreMoney':
        break
    if float(input_field) < 0:
        print(f'Invalid operation!')
        break
    command = float(input_field)
    sums += command
    print(f'Increase: {command:.2f}')

    input_field = input()

print(f'Total: {sums:.2f}')
