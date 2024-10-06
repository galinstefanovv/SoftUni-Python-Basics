day = input()
days = 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'

if day == 'Sunday' or day == 'Saturday':
    print(f'Weekend')
elif day not in days:
    print(f'Error')
else:
    print(f'Working day')