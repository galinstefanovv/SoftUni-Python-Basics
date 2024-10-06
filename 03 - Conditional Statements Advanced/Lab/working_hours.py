hour = int(input())
day = input()
days = 'Monday, Tuesday, Wednesday, Thursday, Friday, Saturday'

if day in days and 10 <= hour <= 18:
    print('open')
else:
    print('closed')