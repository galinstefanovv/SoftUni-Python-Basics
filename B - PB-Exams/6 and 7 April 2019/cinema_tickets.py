input_line = input()
student = 0
standard = 0
kids = 0
count_total = 0
while input_line != "Finish":
    free_space = int(input())
    count = 0
    while count < free_space:
        type = input()
        if type == "student":
            student += 1
        elif type == "standard":
            standard += 1
        elif type == "kid":
            kids += 1
        if type == "End":
            break
        count += 1
        count_total += 1
        percentage = count / free_space
    print(f'{input_line} - {percentage * 100:.2f}% full.')
    input_line = input()
print(f'Total tickets: {count_total}')
print(f'{(student / count_total) * 100:.2f}% student tickets.')
print(f'{(standard / count_total) * 100:.2f}% standard tickets.')
print(f'{(kids / count_total) * 100:.2f}% kids tickets.')