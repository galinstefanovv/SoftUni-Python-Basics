n = int(input())
sums = 0

while True:
    numbers = int(input())
    sums += numbers
    if sums >= n:
        break

print(sums)