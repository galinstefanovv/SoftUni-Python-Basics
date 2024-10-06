from math import ceil
speed = float(input())
liters = float(input())
total_km = 768800
hours = ceil(total_km / speed) + 3
total_liters = (liters * total_km) / 100
print(hours)
print(f'{total_liters:.0f}')
