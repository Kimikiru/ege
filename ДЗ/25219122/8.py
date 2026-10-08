from itertools import product

letters = sorted("АИКЛМЬ")

for ind, comb in enumerate(product(letters, repeat=6), start=1):
    x = ''.join(comb)
    solve1 = x[0] == "К" and x[-1] == "Ь" and x.count("А") <= 1 and x.count("И") <= 1 and x.count("Л") <= 1 and x.count("М") <= 1
    if x == reversed(solve1)
        