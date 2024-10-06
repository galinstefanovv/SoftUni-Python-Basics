rent = int(input())
figurines = rent - (rent * 0.3)
catering = figurines - (figurines * 0.15)
soundsystem = catering / 2
sum = figurines + catering + soundsystem
print(f'{sum + rent:.2f}')