from math import floor
tournaments_count = int(input())
starting_points = int(input())
points = 0
wins = 0
for tournament in range(tournaments_count):
    stage = input()
    if stage == 'W':
        points += 2000
        wins += 1
    elif stage == 'F':
        points += 1200
    elif stage == 'SF':
        points += 720

print(f'Final points: {starting_points + points}\n'
      f'Average points: {floor(points / tournaments_count)}\n'
      f'{wins / tournaments_count * 100:.2f}%')
