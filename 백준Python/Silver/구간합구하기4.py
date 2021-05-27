import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
d = [0] * (n + 1)

for i in range(1, n + 1):
    d[i] = d[i - 1] + data[i - 1]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(d[b] - d[a - 1])
