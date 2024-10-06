vegetables_price = float(input())
fruit_price = float(input())
vegetables_kg = int(input())
fruit_kg = int(input())
total = vegetables_price * vegetables_kg + fruit_price * fruit_kg
print(f'{total / 1.94:.2f}')