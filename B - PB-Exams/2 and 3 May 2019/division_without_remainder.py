n = int(input())
p1 = 0
p2 = 0
p3 = 0
for i in range(1, n + 1):
    number = int(input())
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1
percentage_p1 = p1 / n * 100
print(f'{percentage_p1:.2f}%')
percentage_p2 = p2 / n * 100
print(f'{percentage_p2:.2f}%')
percentage_p3 = p3 / n * 100
print(f'{percentage_p3:.2f}%')