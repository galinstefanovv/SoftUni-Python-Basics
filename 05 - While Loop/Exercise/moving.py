width = int(input())
length = int(input())
height = int(input())
total_size = width * length * height
data = input()
no_space = False
while data != 'Done':
    cartons = int(data)
    total_size -= cartons
    if total_size <= 0:
        no_space = True
        break
    data = input()

if no_space:
    print(f'No more free space! You need {abs(total_size)} Cubic meters more.')
else:
    print(f'{total_size} Cubic meters left.')