nylon = int(input()) * 1.50
paint = int(input()) * 14.50
thinner = int(input()) * 5
hours = int(input())
paint += paint * 0.1
nylon += 2 * 1.5
expense = nylon + paint + thinner + 0.40
sum_per_hour = expense * 0.3
worker = sum_per_hour * hours
total_sum = expense + worker
print(total_sum)