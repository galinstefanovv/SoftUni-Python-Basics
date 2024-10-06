flour = float(input())
kg_flour = float(input())
kg_sugar = float(input())
eggs = int(input())
yeast = int(input())
sugar_p = flour * 0.75
eggs_p = flour + (flour * 0.1)
yeast_p = sugar_p * 0.2
total = (flour * kg_flour) + (sugar_p * kg_sugar) + (eggs_p * eggs) + (yeast_p * yeast)
print(f'{total:.2f}')