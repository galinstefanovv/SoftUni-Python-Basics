import sys
breads = int(input())
max = -sys.maxsize
name = ""
for i in range(1, breads + 1):
    best = False
    baker = input()
    input_line = input()
    rate_total = 0
    while input_line != "Stop":
        rate = int(input_line)
        rate_total += rate
        if rate_total > max:
            max = rate_total
            name = baker
            best = True
        input_line = input()
    print(f'{baker} has {rate_total} points.')
    if best:
        print(f'{name} is the new number 1!')
print(f'{name} won competition with {max} points!')
