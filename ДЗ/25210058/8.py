from itertools import product

letters = sorted("ЯЩЕР")

counter=0

for index, comb in enumerate(product(letters, repeat=5), start=1):
    x=''.join(comb)
    if x.count("Е") < 3:
        counter += 1

print(counter)