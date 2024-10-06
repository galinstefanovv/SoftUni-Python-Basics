fuel = input()
liters = int(input())
valid_fuels = 'Diesel', 'Gasoline', 'Gas'
if fuel in valid_fuels:
    if liters >= 25:
        print(f'You have enough {fuel.lower()}.')
    else:
        print(f'Fill your tank with {fuel.lower()}!')
else:
    print(f'Invalid fuel!')