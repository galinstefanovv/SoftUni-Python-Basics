cargo = int(input())
price = 0
van = 0
truck = 0
train = 0
total_tons = 0
for i in range(cargo):
    tons = int(input())
    total_tons += tons
    if tons <= 3:
        price += 200 * tons
        van += tons
    elif 4 <= tons <= 11:
        price += 175 * tons
        truck += tons
    else:
        price += 120 * tons
        train += tons

average_price = price / total_tons

print(f'{average_price:.2f}\n'
      f'{van / total_tons * 100:.2f}%\n'
      f'{truck / total_tons * 100:.2f}%\n'
      f'{train / total_tons * 100:.2f}%')