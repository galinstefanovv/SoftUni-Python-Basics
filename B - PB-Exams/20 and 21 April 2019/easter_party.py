guests = int(input())
price = float(input())
budget = float(input())
total = 0
if 10 <= guests <= 15:
    price *= 0.85
elif 15 < guests <= 20:
    price *= 0.8
elif guests > 20:
    price *= 0.75
cake = budget * 0.1

sum = (price * guests) + cake

if sum <= budget:
    print(f'It is party time! {abs(sum - budget):.2f} leva left.')
else:
    print(f'No party! {abs(sum - budget):.2f} leva needed.')