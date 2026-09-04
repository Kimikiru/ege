f=open('17-4.txt')
listed=[]
for str in f:
        listed.append(int(str))

counter=0
minDvashkai=[]

maxi69 = [x for x in listed if x % 100 == 69]
maxi=max(maxi69)

mini=[]
mini17 = [x for x in listed if x > 0]
for g in mini17:
        if g % 17 == 0:
                mini.append(g)
summOfMini=sorted(mini)[0] + sorted(mini)[1]


minimum=float('inf')

for indexx in range(0, len(listed)-3):
    t1 = 99 < listed[indexx] < 1000
    t2 = 99 < listed[indexx+1] < 1000
    t3 = 99 < listed[indexx+2] < 1000
    t4 = 99 < listed[indexx+3] < 1000
    del1 = listed[indexx] % 18 == 0
    del2 = listed[indexx+1] % 18 == 0
    del3 = listed[indexx+2] % 18 == 0
    del4 = listed[indexx+3] % 18 == 0
    if (listed[indexx] + listed[indexx+1] + listed[indexx+2] +listed[indexx+3]) %summOfMini ==0 and (listed[indexx] * listed[indexx+1] * listed[indexx+2] * listed[indexx+3]) <= maxi and t1 + t2 + t3 + t4 == 2 and del1 + del2 + del3 + del4 == 1:
        counter+=1
        minimum=min((listed[indexx] * listed[indexx+1] * listed[indexx+2] * listed[indexx+3])**2, minimum)           
print(counter, minimum)
