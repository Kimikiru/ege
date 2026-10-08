maxximki = []
listed = []
counter=0

with open("17.txt") as f:
    for x in f:
        listed.append(int(x))

maxx = [x for x in listed if abs(x) % 1000 == 121]
maxx = max(maxx)

for index in range(0, len(listed)-2):
    part1 = 1000 <= abs(listed[index]) <= 9999 and listed[index] % 2 == 0
    part2 = 1000 <= abs(listed[index+1]) <= 9999 and listed[index+1] % 2 == 0
    part3 = 1000 <= abs(listed[index+2]) <= 9999 and listed[index+2] % 2 == 0
    if part1 + part2 + part3 <= 1 and listed[index] + listed[index+1] + listed[index+2] <= maxx:
        counter+=1
        maxximki.append(listed[index] + listed[index+1] + listed[index+2])
print(counter, max(maxximki))