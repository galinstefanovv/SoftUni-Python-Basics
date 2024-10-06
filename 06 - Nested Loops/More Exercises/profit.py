one_lv = int(input())
two_lv = int(input())
five_lv = int(input())
sums = int(input())

for i in range(0, one_lv + 1):
    for j in range(0, two_lv + 1):
        for k in range(0, five_lv + 1):
            total = i + j * 2 + k * 5
            if total == sums:
                print(f'{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {sums} lv.')