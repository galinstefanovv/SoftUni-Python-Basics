v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())
p1_l = p1 * h
p2_l = p2 * h
total_l = p1_l + p2_l
total_percent = (total_l/v) * 100
if v >= total_l:
    print(f'The pool is {total_percent:.2f}% full. Pipe 1: {(p1_l/total_l)*100:.2f}%. Pipe 2: {(p2_l/total_l)*100:.2f}%.')
else:
    diff = total_l - v
    print(f'For {h:.2f} hours the pool overflows with {diff:.2f} liters.')