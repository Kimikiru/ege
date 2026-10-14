def f(a1, a2, h):
    if a1 + a2 <= 47:
        return h%2==0
    elif h == 0:
        return 0
    pos = [f(a1 - 2, a2, h-1), f(a1, a2 - 2, h-1), f(a1//3, a2, h-1), f(a1, a2//3, h-1)]
    return any(pos) if (h-1) % 2 ==0 else all(pos)

print(19, [s for s in range(32, 400) if any([f(14, s, 1), f(16, s - 2, 1), f(16//3, s, 1), f(16, s//3, 1)])])
print(20, [s for s in range(32, 400) if not f(16, s, 1) and f(16, s, 3)])
print(21, [s for s in range(32, 400) if f(16, s, 4) and not f(16, s, 2)])
