input_line = input()
count_all = 0
student = 0
standard = 0
kid = 0
student_percentage = 0
standard_percentage = 0
kid_percentage = 0
while input_line != "Finish":
    film_name = input_line
    free_space = int(input())
    ticket = input()
    count = 0
    while ticket != "End":
        count += 1
        count_all += 1
        if ticket == "student":
            student += 1
        elif ticket == "standard":
            standard += 1
        elif ticket == "kid":
            kid += 1
        if count >= free_space:
            break
        ticket = input()
    percentage = (count / free_space) * 100
    student_percentage = (student / count_all) * 100
    standard_percentage = (standard / count_all) * 100
    kid_percentage = (kid / count_all) * 100
    print(f'{film_name} - {percentage:.2f}% full.')
    input_line = input()

print(f'Total tickets: {count_all}')
print(f'{student_percentage:.2f}% student tickets.')
print(f'{standard_percentage:.2f}% standard tickets.')
print(f'{kid_percentage:.2f}% kids tickets.')