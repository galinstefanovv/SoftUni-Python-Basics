pages = int(input())
pages_per_hour = int(input())
days = int(input())

total = (pages // pages_per_hour) // days

print(total)