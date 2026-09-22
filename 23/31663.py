edges = []
W = {}
for line in open('23_31663.txt'):
    if not line.strip():
        continue
    a, b, w = line.split()
    a, b, w = int(a), int(b), float(w)
    edges.append((a,b,w))

starts = {a for a, b, w in edges}


INF = float('inf')
d = {2027: 0}
changed = True
while changed:
    changed = False
    for a, b, w in edges:
        if a in d and d[a] + w > d.get(b, -INF):
            d[b] = d[a] + w
            changed = True

print(int(max(d[v] for v in d if v not in starts)))