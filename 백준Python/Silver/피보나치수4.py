n = int(input())
d = [0] * 10001
d[0], d[1], d[2] = 0, 1, 1
for i in range(3, n + 1):
    d[i] = d[i - 2] + d[i - 1]
print(d[n])
