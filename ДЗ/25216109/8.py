from itertools import product

listed = []

letters = sorted("КАРЕТ")
for ind, word in enumerate(product(letters, repeat=6), start=1):
    x = ''.join(word)
    listed.append(x)

print(listed.index("РАКЕТА") - listed.index("КАРЕТА"))