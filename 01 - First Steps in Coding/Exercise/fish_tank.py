length = int(input())
width = int(input())
height = int(input())
percent = int(input())

volume = length * width * height
volume_liters = volume * 0.001
total = volume_liters * (1 - percent/100)

print(total)