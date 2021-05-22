n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(3):
        if j == 0:
            data[i][j] = min(data[i - 1][1], data[i - 1][2]) + data[i][j]
        elif j == 1:
            data[i][j] = min(data[i - 1][0], data[i - 1][2]) + data[i][j]
        elif j == 2:
            data[i][j] = min(data[i - 1][0], data[i - 1][1]) + data[i][j]

print(min(data[-1]))
