bread = int(input()) * 3.20
eggs = int(input())
cookies = int(input()) * 5.40
eggs_p = eggs * 4.35
eggs_t = eggs * 12
total = bread + eggs_p + cookies + (eggs_t * 0.15)
print(f'{total:.2f}')
