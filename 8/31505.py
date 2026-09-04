from itertools import product

letters = "АЕКНТЦ"

for index, combo in enumerate(product(letters, repeat=5), start=1):
    word = ''.join(combo)

    if index % 2 != 0:
        continue
    if word[0] in 'АЕК':
        continue
    if word.count("Т") < 1:
        continue    
        
    print(index)
    break