tab_count = int(input())
salary = int(input())
lost = False
for tabs in range(tab_count):
    website = input()
    if website == 'Facebook':
        salary -= 150
    elif website == 'Instagram':
        salary -= 100
    elif website == 'Reddit':
        salary -= 50

    if salary <= 0:
        lost = True
        break

if lost:
    print(f'You have lost your salary.')
else:
    print(f'{salary}')
