ans = []

def tri(n):
    N = ""
    while n > 0:
        N += str(n % 3)
        n //= 3
    return N[::-1] 

for N in range(9, 1000):
    s = tri(N)
    summ = (s.count("1") + 2 * s.count("2")) % 9
    if summ == 0:
        s = s + "2"
    else:
        s = s + tri(summ)
    if N > 166:
        ans.append((int(s, 3)))

print(min(ans))


# тут ошибку понял, опять же, надо было нормально читать задание
