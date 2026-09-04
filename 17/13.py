with open("13.txt") as f:
    sp=[int(line) for line in f]

N = 999999
for x in sp:
    if x % 15 != 0:
        N = min(N, x)
maxsum = 0
k = 0
for i in range(len(sp) - 1):
    p1 = sp[i] % N == 0
    p2 = sp[i + 1] % N == 0
    if p1 + p2 == 2:
        maxsum = max(maxsum, sp[i] + sp[i + 1])
        k += 1
print(k, maxsum)