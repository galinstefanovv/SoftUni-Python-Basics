m = int(input())
notfound = False
count = 0
output = ''
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                total = a * b + c * d
                if a < b and c > d and total == m:
                    count += 1
                    print(f'{a}{b}{c}{d}', end=' ')
                    if count == 4:
                        output = f'{a}{b}{c}{d}'

if count < 4:
    print(f'\nNo!')
else:
    print(f'\nPassword: {output}')