width = float(input())
height = float(input())
rows = ((height*100) - 100) // 70
places = (width * 100) // 120
workPlaces = rows * places - 3
print(workPlaces)