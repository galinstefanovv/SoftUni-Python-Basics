kilometers = int(input())
word = input()
price = 0
if kilometers < 20:
    if word == 'day':
        price = (0.79 * kilometers) + 0.70
    elif word == 'night':
        price = (0.90 * kilometers) + 0.70
elif 20 <= kilometers < 100:
    price = 0.09 * kilometers
else:
    price = 0.06 * kilometers

print(f'{price:.2f}')