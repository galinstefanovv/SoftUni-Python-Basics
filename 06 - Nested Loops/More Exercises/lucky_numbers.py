n = int(input())
result = ""
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for m in range(1, 10):
                if (i + j == k + m) and (n % (i + j) == 0):
                    result += str(i) + str(j) + str(k) + str(m) + " "
print(result)