n = int(input())
arrayT = []
arrayP = []
d = [0] * (n + 1)
for _ in range(n):
    t, p = map(int, input().split())
    arrayT.append(t)
    arrayP.append(p)
for i in range(n - 1, -1, -1):
    if arrayT[i] + i > n:
        d[i] = d[i + 1]
    else:
        d[i] = max(d[i + 1], arrayP[i] + d[i + arrayT[i]])
print(d[0])
