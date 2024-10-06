x = float(input())
y = float(input())
h = float(input())

one_wall = x*y
one_window = 1.5*1.5
two_walls = one_wall * 2 - one_window * 2

back_wall = x*x
entrance = 1.2*2

back_entr = 2 * back_wall - entrance

total_area = two_walls + back_entr
green_paint = total_area / 3.4
print(format(green_paint, ".2f"))

prav_pokr = 2*(x*y)
triugl = 2*(x*h/2)
total_area_pokr = prav_pokr+triugl
red_paint = total_area_pokr / 4.3
print(format(red_paint, ".2f"))