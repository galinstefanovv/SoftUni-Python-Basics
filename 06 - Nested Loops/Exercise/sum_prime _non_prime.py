data = input()
prime = 0
non_prime = 0
while data != 'stop':
    numbers = int(data)
    counter = 0
    if numbers < 0:
        print(f'Number is negative.')
        data = input()
        continue
    for num in range(1, numbers + 1):
        if numbers % num == 0:
            counter += 1
    if counter > 2:
        non_prime += numbers
    else:
        prime += numbers

    data = input()

print(f'Sum of all prime numbers is: {prime}\n'
      f'Sum of all non prime numbers is: {non_prime}')