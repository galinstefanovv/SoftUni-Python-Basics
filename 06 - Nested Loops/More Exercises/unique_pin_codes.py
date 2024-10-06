start = int(input())
mid = int(input())
end = int(input())
for i in range(2, start + 1, 2):
    for j in range(2, mid + 1):
        for k in range(2, end + 1, 2):
            if j == 2 or j == 3 or j == 5 or j == 7:
                print(f'{i} {j} {k}')