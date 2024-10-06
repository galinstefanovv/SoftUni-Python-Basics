first = input()
second = input()
third = input()
won = 0
lost = 0
drawn = 0
if first[0] > first[2]:
    won += 1
if second[0] > second[2]:
    won +=1
if third[0] > third[2]:
    won +=1

if first[0] < first[2]:
    lost += 1
if second[0] < second[2]:
    lost +=1
if third[0] < third[2]:
    lost +=1

if first[0] == first[2]:
    drawn += 1
if second[0] == second[2]:
    drawn +=1
if third[0] == third[2]:
    drawn +=1

print(f'Team won {won} games.')
print(f'Team lost {lost} games.')
print(f'Drawn games: {drawn}')