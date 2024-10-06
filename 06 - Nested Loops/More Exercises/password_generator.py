n = int(input())
l = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(ord('a'), ord('a') + l):
            for s in range(ord('a'), ord('a') + l):
                for m in range(max(i, j) + 1, n + 1):
                    print(f'{i}{j}{chr(k)}{chr(s)}{m}',end = ' ')