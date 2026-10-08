with open("9-24359.txt") as f:
    sp = [[int(x) for x in line.split()] for line in f]

counter = 0

for x in sp:
    pov = [i for i in x if x.count(i) == 3]
    tov = [i for i in x if x.count(i) == 2]
    if len(pov) == 3 and len(tov) == 2:
        nepov = [i for i in x if x.count(i) == 1]
        sum_pov = sum(pov) + sum(tov)
        sum_nepov = sum(nepov)
        if sum_pov > sum_nepov:
            counter = sum(x)

print(counter)