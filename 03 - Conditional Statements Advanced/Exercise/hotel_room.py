month = input()
stay = int(input())
studio = 0
apartment = 0

if month == 'May' or month == 'October':
    studio = 50 * stay
    apartment = 65 * stay
    if stay > 14:
        studio -= studio * 0.3
    elif stay > 7:
        studio -= studio * 0.05
elif month == "June" or month == "September":
    studio = 75.2 * stay
    apartment = 68.7 * stay
    if stay > 14:
        studio -= studio * 0.2
elif month == "July" or month == "August":
    studio = 76 * stay
    apartment = 77 * stay

if stay > 14:
    apartment -= apartment * 0.1

print(f'Apartment: {apartment:.2f} lv.\n'
      f'Studio: {studio:.2f} lv.')
