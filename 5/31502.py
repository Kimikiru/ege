listed = []

for N in range(1,10000):
    
    bin_N = bin(N)[2:]
    if N % 2 == 0:
        bin_N = "11" + bin_N + "11"
    
    else:
        bin_N = "1" + bin_N + "00"

    R = int(bin_N, 2)
    if R > 95:
        listed.append(R)
print(min(listed))