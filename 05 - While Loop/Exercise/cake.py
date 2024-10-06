width = int(input())
length = int(input())
total_size = width * length
input_field = input()
over = False
while input_field != 'STOP':
    size = int(input_field)
    total_size -= size
    if total_size <= 0:
        over = True
        break
    input_field = input()

if over:
    print(f'No more cake left! You need {abs(total_size)} pieces more.')
else:
    print(f'{total_size} pieces are left.')
