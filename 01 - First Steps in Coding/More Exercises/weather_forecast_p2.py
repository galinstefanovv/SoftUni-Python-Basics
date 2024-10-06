degree = float(input())

if 26 <= degree <= 35:
    print(f'Hot')
elif 20.1 <= degree <= 25.9:
    print(f'Warm')
elif 15 <= degree <= 20:
    print('Mild')
elif 12 <= degree <= 14.9:
    print(f'Cool')
elif 5 <= degree <= 11.9:
    print(f'Cold')
else:
    print(f'unknown')