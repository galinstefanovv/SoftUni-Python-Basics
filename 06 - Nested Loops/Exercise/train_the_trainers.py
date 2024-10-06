judges = int(input())
presentation = input()
total_grades = 0
grades_counter = 0
while presentation != 'Finish':
    total_grades_per_presentation = 0
    average_per_presentation = 0
    for grade in range(1, judges + 1):
        grades = float(input())
        grades_counter += 1
        total_grades_per_presentation += grades
        average_per_presentation = total_grades_per_presentation / judges
    print(f'{presentation} - {average_per_presentation:.2f}.')
    total_grades += total_grades_per_presentation
    presentation = input()

print(f"Student's final assessment is {total_grades / grades_counter:.2f}.")