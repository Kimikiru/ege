f=open('17-3.txt')
listed=[]
for str in f:
        listed.append(int(str))

counter=0
multiples_of_10s = [x for x in listed if x % 100 == 10]
max_10s = max(multiples_of_10s)

minimum=float('inf')

for indexx in range(0, len(listed)-1):
	if (listed[indexx] % 2023) * (listed[indexx+1] % 2023) >= max_10s:        
                counter += 1
                minimum=min(minimum, listed[indexx] + listed[indexx+1])

print(counter, minimum)
