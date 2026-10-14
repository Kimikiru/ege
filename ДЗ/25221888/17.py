listed = []
minn = float('inf')

maxx_duo = []
counter = 0

with open('17.txt') as f:
    for x in f:
        x = int(x)
        listed.append(x)
        if abs(x) < minn:
            minn = abs(x)

for ind in range(1, len(listed) - 1):
    checker = 0
    part1 = listed[ind]
    part2 = listed[ind+1]
    
    if part1 < 0:
        checker +=1
    if part2 < 0:
        checker +=1
    
    if checker == 1 and part1 + part2 > 0 and (part1 + part2) % minn == 0:
        maxx_duo.append(part1 + part2)
        counter += 1

print(counter, max(maxx_duo))