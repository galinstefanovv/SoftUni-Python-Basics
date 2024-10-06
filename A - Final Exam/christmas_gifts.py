input_line = input()
sum_toy = 0
sum_shirt = 0
toy = 0
shirt = 0
while input_line != "Christmas":
    age = int(input_line)
    if age <= 16:
        toy += 1
        sum_toy += 5
    elif age > 16:
        shirt += 1
        sum_shirt += 15
    input_line = input()
print(f'Number of adults: {shirt}')
print(f'Number of kids: {toy}')
print(f'Money for toys: {sum_toy}')
print(f'Money for sweaters: {sum_shirt}')