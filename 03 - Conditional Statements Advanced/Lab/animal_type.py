animal = input()

mammal = 'dog'
reptile = 'crocodile', 'tortoise', 'snake'

if animal in mammal:
    print(f'mammal')
elif animal in reptile:
    print(f'reptile')
else:
    print('unknown')