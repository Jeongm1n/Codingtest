d = [[0] * 4 for _ in range(100001)]
d[1][1], d[2][2], d[3][1], d[3][2], d[3][3] = 1, 1, 1, 1, 1

for i in range(4, 100001):
    for j in range(1, 4):
        d[i][j] = (sum(d[i - j]) - d[i - j][j]) % 1000000009
for _ in range(int(input())):
    n = int(input())
    print(sum(d[n]) % 1000000009)
