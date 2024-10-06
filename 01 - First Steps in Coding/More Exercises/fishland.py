mackerel_price = float(input())
sprat_price = float(input())
bonito_kg = float(input())
saffron_kg = float(input())
mussels_kg = float(input())

bonito_price = bonito_kg * (mackerel_price + mackerel_price * 0.6)
saffron_price = saffron_kg * (sprat_price + sprat_price * 0.8)
mussels_price = mussels_kg * 7.5

total_price = bonito_price + saffron_price + mussels_price

print(f'{total_price:.2f}')
