season = input()
group_type = input()
students = int(input())
nights = int(input())
sport = ''
price = 0
if season == 'Winter':
    price = 9.60 * nights * students
    if group_type == 'girls':
        sport = 'Gymnastics'
    elif group_type == 'boys':
        sport = 'Judo'
    elif group_type == 'mixed':
        sport = 'Ski'
        price += (0.4 * nights * students)
elif season == 'Spring':
    price = 7.20 * nights * students
    if group_type == 'girls':
        sport = 'Athletics'
    elif group_type == 'boys':
        sport = 'Tennis'
    elif group_type == 'mixed':
        sport = 'Cycling'
        price += (2.30 * nights * students)
elif season == 'Summer':
    price = 15 * nights * students
    if group_type == 'girls':
        sport = 'Volleyball'
    elif group_type == 'boys':
        sport = 'Football'
    elif group_type == 'mixed':
        sport = 'Swimming'
        price += (5 * nights * students)

if students >= 50:
    price *= 0.5
elif 20 <= students < 50:
    price *= 0.85
elif 10 <= students < 20:
    price *= 0.95

print(f'{sport} {price:.2f} lv.')
