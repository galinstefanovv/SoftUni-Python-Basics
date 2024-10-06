type = input()
rows = int(input())
cols = int(input())
total = rows * cols

if type == 'Premiere':
    income = total * 12
elif type == 'Normal':
    income = total * 7.5
else:
    income = total * 5

print(f'{income:.2f} leva')