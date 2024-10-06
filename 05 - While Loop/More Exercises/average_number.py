n = int(input())
count = 0
total = 0
for i in range(n):
    num = int(input())
    count += 1
    total += num

print(f'{total / count:.2f}')