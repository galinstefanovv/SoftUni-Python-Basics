book = input()
search = input()
found = False
count = 0
while search != 'No More Books':
    if search == book:
        found = True
        break
    else:
        count += 1
    search = input()

if found:
    print(f'You checked {count} books and found it.')
else:
    print(f'The book you search is not here!\n'
          f'You checked {count} books.')

