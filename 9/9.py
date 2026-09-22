import math

with open("9.txt") as f:
    sp = [[int(x) for x in line.split()] for line in f]

k = 0

for x in sp:
    pov = [i for i in x if x.count(i) == 3]
    np = [i for i in x if x.count(i) == 1]
    if len(pov) == 3 and len(np) == 3:
        if pov[0] ** 3 < np[0]*np[1]*np[2]:
            k+=1
print(k)