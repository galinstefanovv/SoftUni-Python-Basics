trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

total_count = puzzles + dolls + bears + minions + trucks
total_sum = puzzles * 2.6 + dolls * 3 + bears * 4.1 + minions * 8.2 + trucks * 2

if total_count >= 50:
    total_sum -= total_sum * 0.25

tax = total_sum * 0.1

total_price = total_sum - tax

if total_price >= trip_price:
    print(f'Yes! {total_price - trip_price:.2f} lv left.')
else:
    print(f'Not enough money! {abs(total_price - trip_price):.2f} lv needed.')