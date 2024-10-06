start = int(input())
end = int(input())
magic_number = int(input())
count = 0
isfound = False
for i in range(start, end + 1):
    for j in range(start, end + 1):
        sums = i + j
        count += 1
        if sums == magic_number:
            print(f'Combination N:{count} '
                  f'({i} + {j} = {magic_number})')
            isfound = True
            break
    if isfound:
        break

if not isfound:
    print(f'{count} combinations - neither equals {magic_number}')

