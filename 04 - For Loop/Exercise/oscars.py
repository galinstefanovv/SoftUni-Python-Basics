actor = input()
academy_points = float(input())
judge_count = int(input())
points_needed = 1250.5
nomination = False

for judge in range(judge_count):
    judge_name = input()
    judge_points = float(input())
    academy_points += len(judge_name) * judge_points / 2

    if academy_points > points_needed:
        nomination = True
        break

if nomination:
    print(f'Congratulations, {actor} got a nominee for leading role with {academy_points:.1f}!')
else:
    print(f'Sorry, {actor} you need {abs(academy_points - points_needed):.1f} more!')