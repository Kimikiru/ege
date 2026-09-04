listed = []

for N in range(1, 10000):
    bin_N = bin(N)[2:]

    if N % 2 == 0:
        bin_N = "10" + bin_N
    else:
        bin_N = "1" + bin_N + "01"
    
    R = int(bin_N, 2)

    if N >= 17:
        listed.append(R)

print(min(listed))