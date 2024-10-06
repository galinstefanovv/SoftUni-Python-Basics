trekking_group = int(input())
musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_people = 0

for group in range(trekking_group):
    group_count = int(input())
    total_people += group_count
    if group_count <= 5:
        musala += group_count
    elif 6 <= group_count <= 12:
        mont_blanc += group_count
    elif 13 <= group_count <= 25:
        kilimanjaro += group_count
    elif 26 <= group_count <= 40:
        k2 += group_count
    else:
        everest += group_count

musala = musala / total_people * 100
mont_blanc = mont_blanc / total_people * 100
kilimanjaro = kilimanjaro / total_people * 100
k2 = k2 / total_people * 100
everest = everest / total_people * 100

print(f'{musala:.2f}%\n'
      f'{mont_blanc:.2f}%\n'
      f'{kilimanjaro:.2f}%\n'
      f'{k2:.2f}%\n'
      f'{everest:.2f}%\n')