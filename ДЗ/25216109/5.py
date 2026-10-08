def ternary(N):
    res = []
    while N > 0:
        res.append(str(N%3))
        N //= 3
    return "".join(reversed(res))



for N in range(1, 1000):
    s = ternary(N)
    digits_count = s.count("2") + s.count("1")
    if digits_count % 4 == 0:
        s = "1" + s[:2]
    else:
        s = s + ternary(digits_count * 3)

    R = int(s, 3)
    if R > 353:
        print(R)
        break