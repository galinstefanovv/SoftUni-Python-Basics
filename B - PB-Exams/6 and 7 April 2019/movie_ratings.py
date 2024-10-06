import sys
count = int(input())
max_num = -sys.maxsize
min_num = sys.maxsize
film_max = ""
film_min = ""
count1 = 0
sum = 0
for i in range(1, count + 1):
    film = input()
    rating = float(input())
    count1 += 1
    sum += rating
    if rating > max_num:
        max_num = rating
        film_max = film
    if rating < min_num:
        min_num = rating
        film_min = film

print(f'{film_max} is with highest rating: {max_num:.1f}')
print(f'{film_min} is with lowest rating: {min_num:.1f}')
print(f'Average rating: {sum / count:.1f}')