listed_max = []

for N in range(1, 1000):
    bin_N = bin(N)[3:]
    counter = bin_N.count("1")
    if counter % 2 == 0:
        bin_N = "10" + bin_N
    else:
        bin_N = "1" + bin_N + '0'
    if int(bin_N, 2) < 450:
        listed_max.append(int(bin_N, 2))
print(max(listed_max))




