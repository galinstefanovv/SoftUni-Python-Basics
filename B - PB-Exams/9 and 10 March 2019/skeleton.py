m = int(input())
s= int(input())
length = float(input())
seconds_100_meters = int(input())
minutes = m * 60
total_m_s = minutes + s
minus = (length / 120) * 2.5
total = ((length / 100) * seconds_100_meters) - minus
if total <= total_m_s:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {total:.3f}.')
else:
    print(f'No, Marin failed! He was {abs(total_m_s - total):.3f} second slower.')



