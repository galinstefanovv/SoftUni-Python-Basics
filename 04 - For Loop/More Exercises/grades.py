students = int(input())
total_grade = 0
poor_grade = 0
average_grade = 0
good_grade = 0
excellent_grade = 0
for student in range(students):
    grade = float(input())
    total_grade += grade
    if 2 <= grade <= 2.99:
        poor_grade += 1
    elif 3 <= grade <= 3.99:
        average_grade += 1
    elif 4 <= grade <= 4.99:
        good_grade += 1
    else:
        excellent_grade += 1

print(f'Top students: {excellent_grade / students * 100:.2f}%\n'
      f'Between 4.00 and 4.99: {good_grade / students * 100:.2f}%\n'
      f'Between 3.00 and 3.99: {average_grade / students * 100:.2f}%\n'
      f'Fail: {poor_grade / students * 100:.2f}%\n'
      f'Average: {total_grade / students:.2f}')