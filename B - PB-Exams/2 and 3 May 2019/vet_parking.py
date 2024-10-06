days = int(input())
hours = int(input())
total = 0
for i in range(1, days + 1):
    sum = 0
    for j in range(1, hours + 1):
        if i % 2 == 0 and j % 2 != 0:
            sum += 2.50
        elif i % 2 != 0 and j % 2 == 0:
            sum += 1.25
        else:
            sum += 1
    total += sum
    print(f'Day: {i} - {sum:.2f} leva')
print(f'Total: {total:.2f} leva')