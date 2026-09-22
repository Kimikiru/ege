edges = []
W = {}
for line in open('23_31673.txt'):
    if not line.strip():
        continue
    a, b, w = line.split()
    a, b, w = int(a), int(b), float(w)
    edges.append((a, b, w))
    W[a, b] = w

INF = float('inf')
d = {2840: 0}
changed = True
while changed:
    changed = False
    for a, b, w in edges:
        if a in d and d[a] + w < d.get(b, INF):
            d[b] = d[a] + w
            changed = True

print(int(W[2691, 2840] + d[9180] + W[9180, 9514]))