start = int(input())
end = int(input())
magic_number = int(input())
count = 0
sums = 0
founded = False
for fn in range(start, end + 1):
    for sn in range(start, end + 1):
        sums = fn + sn
        count += 1
        if sums == magic_number:
            founded = True
            print(f'Combination N:{count} ({fn} + {sn} = {magic_number})')
            break
    if founded:
        break
if not founded:
    print(f'{count} combinations - neither equals {magic_number}')

