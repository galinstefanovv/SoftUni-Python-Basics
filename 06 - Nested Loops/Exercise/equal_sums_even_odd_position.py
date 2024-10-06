start = int(input())
end = int(input())
for i in range(start, end + 1):
    number_str = str(i)
    even = 0
    odd = 0
    for index,digit in enumerate(number_str):
        if index % 2 == 0:
            even += int(digit)
        else:
            odd += int(digit)
    if even == odd:
        print(f'{i}', end= ' ')