customers = int(input())
total = 0
for i in range(1, customers + 1):
    input_line = input()
    count = 0
    sum = 0

    while input_line != "Finish":
        count += 1
        if input_line == "basket":
            sum += 1.50
        elif input_line == "wreath":
            sum += 3.80
        elif input_line == "chocolate bunny":
            sum += 7
        input_line = input()
    if count % 2 == 0:
        sum *= 0.8
    total += sum
    print(f'You purchased {count} items for {sum:.2f} leva.')
print(f'Average bill per client is: {total / customers:.2f} leva.')