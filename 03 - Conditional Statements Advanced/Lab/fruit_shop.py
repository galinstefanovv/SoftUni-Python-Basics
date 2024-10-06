fruit = input()
day = input()
qty = float(input())
work_days = 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'
weekdays = 'Saturday', 'Sunday'
correct = True
price = 0

if day in work_days:
    if fruit == 'banana':
        price = qty * 2.5
    elif fruit == 'apple':
        price = qty * 1.2
    elif fruit == 'orange':
        price = qty * 0.85
    elif fruit == 'grapefruit':
        price = qty * 1.45
    elif fruit == 'kiwi':
        price = qty * 2.7
    elif fruit == 'pineapple':
        price = qty * 5.5
    elif fruit == 'grapes':
        price = qty * 3.85
    else:
        correct = False
elif day in weekdays:
    if fruit == 'banana':
        price = qty * 2.7
    elif fruit == 'apple':
        price = qty * 1.25
    elif fruit == 'orange':
        price = qty * 0.9
    elif fruit == 'grapefruit':
        price = qty * 1.6
    elif fruit == 'kiwi':
        price = qty * 3
    elif fruit == 'pineapple':
        price = qty * 5.6
    elif fruit == 'grapes':
        price = qty * 4.2
    else:
        correct = False
else:
    correct = False

if correct:
    print(f'{price:.2f}')
else:
    print(f'error')

