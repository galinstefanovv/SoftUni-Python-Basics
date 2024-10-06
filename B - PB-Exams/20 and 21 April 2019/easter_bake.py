from math import ceil
import sys
bread = int(input())
sugar_total = 0
flour_total = 0
max_sugar = -sys.maxsize
max_flour = -sys.maxsize
for i in range(1, bread + 1):
    sugar = int(input())
    flour = int(input())
    sugar_total += sugar
    flour_total += flour
    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour
print(f'Sugar: {ceil(sugar_total / 950)}')
print(f'Flour: {ceil(flour_total / 750)}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')


