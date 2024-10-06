man = int(input())
woman = int(input())
tables = int(input())
count = 0
for i in range(1, man + 1):
    for k in range(1, woman + 1):
        count += 1
        print(f'({i} <-> {k})', end=" ")
        if count >= tables:
            break
    if count >= tables:
        break