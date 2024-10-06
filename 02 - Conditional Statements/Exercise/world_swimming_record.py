from math import floor

record_s = float(input())
distance = float(input())
time_s = float(input())

total_time = distance * time_s
delay = floor(distance / 15)
total_delay = delay * 12.5

check = total_time + total_delay

if check < record_s:
    print(f'Yes, he succeeded! The new world record is {check:.2f} seconds.')
else:
    print(f'No, he failed! He was {abs(check - record_s):.2f} seconds slower.')