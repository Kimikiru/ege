from itertools import product

chet = '246'

counter = 0
for i in product('01234567', repeat = 4):
    x = ''.join(i)
    if x[0] in chet and list(x) == sorted(x, reverse=True):
        counter += 1

print(counter)