walking = input()
goal = 10000
sums = 0
is_reached = False
while walking != "Going home":
    steps = int(walking)
    sums += steps

    if sums >= goal:
        break
    walking = input()
if walking == "Going home":
    steps_home = int(input())
    sums += steps_home
diff = abs(sums - goal)
if sums >= goal:
    print(f'Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')