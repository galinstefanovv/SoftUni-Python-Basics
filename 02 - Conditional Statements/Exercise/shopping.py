budget = float(input())
video_card = int(input())
processor = int(input())
ram = int(input())

video_price = video_card * 250
processor_price = processor * video_price * 0.35
ram_price = ram * video_price * 0.1

total_price = video_price + processor_price + ram_price

if video_card > processor:
    total_price -= total_price * 0.15

diff = abs(budget - total_price)

if budget >= total_price:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')