import sys
team = input()  # Argentina, Brazil , Croatia , Denmark
type = input()  # flags, caps, posters, stickers
qty = int(input())
sums = 0

if team == "Argentina":
    if type == "flags":
        sums = 3.25
    elif type == "caps":
        sums = 7.20
    elif type == "posters":
        sums = 5.10
    elif type == "stickers":
        sums = 1.25
    else:
        print("Invalid stock!")
        sys.exit()
elif team == "Brazil":
    if type == "flags":
        sums = 4.20
    elif type == "caps":
        sums = 8.50
    elif type == "posters":
        sums = 5.35
    elif type == "stickers":
        sums = 1.20
    else:
        print("Invalid stock!")
        sys.exit()
elif team == "Croatia":
    if type == "flags":
        sums = 2.75
    elif type == "caps":
        sums = 6.90
    elif type == "posters":
        sums = 4.95
    elif type == "stickers":
        sums = 1.10
    else:
        print("Invalid stock!")
        sys.exit()
elif team == "Denmark":
    if type == "flags":
        sums = 3.10
    elif type == "caps":
        sums = 6.50
    elif type == "posters":
        sums = 4.80
    elif type == "stickers":
        sums = 0.90
    else:
        print("Invalid stock!")
        sys.exit()
else:
    print("Invalid country!")
    sys.exit()
total = sums * qty
print(f'Pepi bought {qty} {type} of {team} for {total:.2f} lv.')

