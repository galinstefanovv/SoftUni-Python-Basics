start = int(input())
end = int(input())
result = ""
for i in range(start, end + 1):
    for j in range(start, end + 1):
        for k in range(start, end + 1):
            for m in range(start, end + 1):
                if i % 2 == 0 and m % 2 != 0 and i > m and (j + k) % 2 == 0:
                    result += str(i) + str(j) + str(k) + str(m) + " "
                elif i % 2 != 0 and m % 2 == 0 and i > m and (j + k) % 2 == 0:
                    result += str(i) + str(j) + str(k) + str(m) + " "
print(result)