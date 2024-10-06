age = int(input())
price_washing = float(input())
price_toy = int(input())
toys = 0
money = 10
sums = 0
brother_count = 0
for birthdays in range(1, age + 1):
    if birthdays % 2 == 0:
        brother_count += 1
        sums = sums + money
        money += 10
    else:
        toys += 1
total_toys = toys * price_toy
total_sum = total_toys + sums - brother_count
if total_sum >= price_washing:
    print(f'Yes! {abs(total_sum - price_washing):.2f}')
else:
    print(f'No! {abs(total_sum - price_washing):.2f}')