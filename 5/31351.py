for N in range(1, 10000):
    bin_N = bin(N)[2:]

    if bin_N.count('1') % 2 == 0:
        bin_N = '10' + bin_N[2:] + '0'
    else:
        bin_N = '11' + bin_N[2:] + '1'

    R = int(bin_N, 2)

    if R >= 16:
        print(N)
        break