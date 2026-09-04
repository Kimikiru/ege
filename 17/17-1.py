f=open('17.txt')
listed=[]
for str in f:
	listed.append(int(str))

counter=0
multiples_of_22 = [x for x in listed if x % 22 == 0]
max_22= max(multiples_of_22)

minimum=float('inf')

for indexx in range(0, len(listed)-1):
	part1=listed[indexx] > max_22
	part2=listed[indexx+1] > max_22
	if part1 + part2 >= 1:
		counter+=1
		minimum=min(minimum, listed[indexx] + listed[indexx+1])

print(counter, minimum)
