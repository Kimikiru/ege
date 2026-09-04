f=open("17-2.txt")
listed=[]
for str in f:
        listed.append(int(str))

counter = 0
maximum = float('-inf')
def NOD(n):
	s = set()
	for i in range(1, int(n**0.5)+1):
		if n % i == 0:
			s.add(i)
			s.add(n//i)
	return s


for indexx in range(0, len(listed)-1):
	if NOD(listed[indexx]) & NOD(listed[indexx+1]):
		if max(NOD(listed[indexx]) & NOD(listed[indexx+1])) > 100:
			counter+=1
			maximum = max(listed[indexx]-listed[indexx+1], maximum)
print(counter, maximum)
