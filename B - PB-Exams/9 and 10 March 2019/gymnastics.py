country = input()
type = input()
points = 0
if country == "Russia":
    if type == "ribbon":
        points += 9.100 + 9.400
    elif type == "hoop":
        points += 9.300 + 9.800
    elif type == "rope":
        points += 9.600 + 9.000
elif country == "Bulgaria":
    if type == "ribbon":
        points += 9.600 + 9.400
    elif type == "hoop":
        points += 9.550 + 9.750
    elif type == "rope":
        points += 9.500 + 9.400
elif country == "Italy":
    if type == "ribbon":
        points += 9.200 + 9.500
    elif type == "hoop":
        points += 9.450 + 9.350
    elif type == "rope":
        points += 9.700 + 9.150
percentage = abs(points - 20)
percentage_2 = (percentage / 20) * 100
print(f'The team of {country} get {points:.3f} on {type}.')
print(f'{percentage_2:.2f}%')