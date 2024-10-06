budget = float(input())
season = input()
destination = ''
place = ''
spend = budget

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        spend *= 0.3
        place = 'Camp'
    elif season == 'winter':
        spend *= 0.7
        place = 'Hotel'
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        spend *= 0.4
        place = 'Camp'
    elif season == 'winter':
        spend *= 0.8
        place = 'Hotel'
else:
    destination = 'Europe'
    spend *= 0.9
    place = 'Hotel'


print(f'Somewhere in {destination}\n'
      f'{place} - {spend:.2f}')