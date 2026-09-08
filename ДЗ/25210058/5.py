answer_massive = []

for N in range(1, 1000):
    bin_N = bin(N)[2:]
    
    if N % 2 == 0:
        bin_N = "10" + bin_N
    else:
        bin_N = "1" + bin_N + "01"

    if int(bin_N, 2) > 441:
        answer_massive.append(N)

print(min(answer_massive))