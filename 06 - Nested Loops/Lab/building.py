floors = int(input())
rooms = int(input())
current_letter = ""
for i in range(floors, 0 , -1):
    for j in range(0, rooms):
        if i == floors:
            current_letter = "L"
        elif i % 2 == 0:
            current_letter = "O"
        else:
            current_letter = "A"
        print(f"{current_letter}{i}{j}", end=" ")
    print()