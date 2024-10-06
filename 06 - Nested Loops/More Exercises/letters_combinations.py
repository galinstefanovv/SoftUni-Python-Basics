first = input()
second = input()
third = input()
count = 0
for f_w in range(ord(first), ord(second) + 1):
    for s_w in range(ord(first), ord(second) + 1):
        for t_w in range(ord(first), ord(second) + 1):
            if third not in chr(f_w) and third not in chr(s_w) and third not in chr(t_w):
                count += 1
                print(f'{chr(f_w)}{chr(s_w)}{chr(t_w)}', end=" ")
print(count)