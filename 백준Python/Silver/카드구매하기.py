import sys

input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))

d = [0] * (n + 1)
d[1], d[2] = card[0], max(card[0] * 2, card[1])

for i in range(3, n + 1):
    d[i] = card[i - 1]
    for j in range(1, i // 2 + 1):
        d[i] = max(d[i], d[j] + d[i - j])

print(d[n])
