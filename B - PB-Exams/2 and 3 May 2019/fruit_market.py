strawberry = float(input())
bananas = float(input())
orange = float(input())
onions = float(input())
strawberry_count = float(input())
onions_money= (strawberry / 2)
onions_sum = onions_money * onions
orange_sum = (onions_money * 0.6) * orange
bananas_sum = (onions_money * 0.2) * bananas
strawberry_sum = strawberry * strawberry_count
total = onions_sum + orange_sum + bananas_sum + strawberry_sum
print(f'{total:.2f}')
