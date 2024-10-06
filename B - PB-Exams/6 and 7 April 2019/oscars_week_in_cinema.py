film = input()
type = input()
tickets = int(input())
price = 0

if film == "A Star Is Born":
    if type == "normal":
        price += 7.50
    elif type == "luxury":
        price += 10.50
    elif type == "ultra luxury":
        price += 13.50
elif film == "Bohemian Rhapsody":
    if type == "normal":
        price += 7.35
    elif type == "luxury":
        price += 9.45
    elif type == "ultra luxury":
        price += 12.75
elif film == "Green Book":
    if type == "normal":
        price += 8.15
    elif type == "luxury":
        price += 10.25
    elif type == "ultra luxury":
        price += 13.25
elif film == "The Favourite":
    if type == "normal":
        price += 8.75
    elif type == "luxury":
        price += 11.55
    elif type == "ultra luxury":
        price += 13.95

print(f'{film} -> {price * tickets:.2f} lv.')
