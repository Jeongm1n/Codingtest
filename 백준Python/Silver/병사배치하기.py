import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
d = [1] * n

for i in range(n):
    for n in range(len(data[:i])):
        if data[i] < data[n] and d[i] < d[n] + 1:
            d[i] = d[n] + 1

print(len(d) - max(d))
