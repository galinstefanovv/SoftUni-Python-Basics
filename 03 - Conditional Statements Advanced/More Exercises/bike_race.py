juniors = int(input())
seniors = int(input())
road = input()
tax_juniors = 0
tax_seniors = 0
if road == 'trail':
    tax_juniors = 5.50 * juniors
    tax_seniors = 7 * seniors
elif road == 'cross-country':
    tax_juniors = 8 * juniors
    tax_seniors = 9.50 * seniors
    if juniors + seniors >= 50:
        tax_juniors *= 0.75
        tax_seniors *= 0.75
elif road == 'downhill':
    tax_juniors = 12.25 * juniors
    tax_seniors = 13.75 * seniors
elif road == 'road':
    tax_juniors = 20 * juniors
    tax_seniors = 21.5 * seniors

total_price = (tax_juniors + tax_seniors) * 0.95

print(f'{total_price:.2f}')