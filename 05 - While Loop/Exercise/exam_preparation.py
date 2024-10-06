bad_grades = int(input())
bad_count = 0
grades_sum = 0
grades_count = 0
last_task = ''
while bad_count != bad_grades:
    task_name = input()
    if task_name == 'Enough':
        break
    grade = int(input())
    if grade <= 4:
        bad_count += 1
    grades_sum += grade
    grades_count += 1
    last_task = task_name

if bad_count >= bad_grades:
    print(f'You need a break, {bad_grades} poor grades.')
else:
    print(f'Average score: {grades_sum / grades_count:.2f}\n'
          f'Number of problems: {grades_count}\n'
          f'Last problem: {last_task}')
