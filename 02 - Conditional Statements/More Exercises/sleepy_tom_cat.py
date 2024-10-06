rest_days = int(input())
total_work = (365 - rest_days) * 63
total_rest = rest_days * 127
total_time = total_work + total_rest
tom_time = abs(total_time - 30000)

if total_time > 30000:
    print(f'Tom will run away\n'
          f'{tom_time // 60} hours and {tom_time % 60} minutes more for play')
else:
    print(f'Tom sleeps well\n'
          f'{tom_time // 60} hours and {tom_time % 60} minutes less for play')