def dl(x):
    divisors = []
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            divisors.append(i)
            if i != x // i:
                divisors.append(x // i)
    return divisors

for x in range(1200000, 1, -1):
    if len(dl(x)) < 3:
        continue
    s = sum(sorted(dl(x), reverse=True)[:3])
    if s != 0 and s % 2022 == 0 and s != x:
        print(x, s)