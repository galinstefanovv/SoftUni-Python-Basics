amount = int(input())
product = input()
sum = 0
count_ticket = 0
count_product = 0
while product != "End":
    if len(product) > 8:
        sum_char = ord(product[0]) + ord(product[1])
        sum += sum_char
        if sum > amount:
            break
        count_ticket += 1
    else:
        sum_char1 = ord(product[0])
        sum += sum_char1
        if sum > amount:
            break
        count_product += 1
    product = input()
print(f'{count_ticket}')
print(f'{count_product}')
