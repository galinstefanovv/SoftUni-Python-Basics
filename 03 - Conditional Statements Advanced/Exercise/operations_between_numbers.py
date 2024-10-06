n1 = int(input())
n2 = int(input())
operator = input()
operators = '+', '-', '*'
result = ''
total = 0
valid = True

if operator in operators:
    if operator == '+':
        total = n1 + n2
    elif operator == '-':
        total = n1 - n2
    else:
        total = n1 * n2
    result = f'{n1} {operator} {n2} = {total} - {"even" if total % 2 == 0 else "odd"}'
elif operator == '/' and not n2 == 0:
    total = n1 / n2
    result = f'{n1} / {n2} = {total:.2f}'
elif operator == '%' and not n2 == 0:
    total = n1 % n2
    result = f'{n1} % {n2} = {total}'
else:
    valid = False

if valid:
    print(result)
else:
    print(f'Cannot divide {n1} by zero')

