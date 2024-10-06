chicken_menu = int(input()) * 10.35
fish_menu = int(input()) * 12.40
veg_menu = int(input()) * 8.15
desert = (chicken_menu + fish_menu + veg_menu) * 0.2
total_sum = chicken_menu + fish_menu + veg_menu + desert + 2.50
print(total_sum)