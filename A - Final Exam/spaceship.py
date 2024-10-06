from math import floor
size = float(input()) * float(input()) * float(input())
av_height = float(input())
v_r = (av_height + 0.40) * 2 * 2
astronauts = floor(size / v_r)

if 3 <= astronauts <= 10:
    print(f'The spacecraft holds {astronauts} astronauts.')
elif astronauts < 3:
    print(f'The spacecraft is too small.')
else:
    print(f'The spacecraft is too big.')


