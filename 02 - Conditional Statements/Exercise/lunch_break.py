import math

series = input()
episode_length = int(input())
rest = int(input())

lunch_time = rest * 1/8
rest_time = rest * 1/4

total_time = rest - lunch_time - rest_time

diff = abs(episode_length - total_time)

if total_time >= episode_length:
    print(f'You have enough time to watch {series} and left with {math.ceil(diff)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series}, you need {math.ceil(diff)} more minutes.")