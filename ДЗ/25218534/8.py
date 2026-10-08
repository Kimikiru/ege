from itertools import product

letters = sorted("МОЛЬ")

counter = 0
for ind, comb in enumerate(product(letters, repeat=5), start=1):
    x = ''.join(comb)
    if x[0] != "Ь" and "ОЬ" not in x and "ЬЬ" not in x:
        counter += 1

print(counter)