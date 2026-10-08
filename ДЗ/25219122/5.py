for N in range(1, 1000):
    binN = bin(N)[2:]
    remains = (N % 3) * 3
    if remains == 0:
        binN = binN + binN[:3]
    else:
        binN =  binN + bin(remains)[2:]
    R = int(binN, 2)
    if R >= 200:
        print(N, R)
        break