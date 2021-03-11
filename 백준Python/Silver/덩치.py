n = int(input())
data = []
answer = [1] * n
for _ in range(n):
    x, y = map(int, input().split())
    data.append((x, y))

for i in range(n-1):
    for j in range(i+1, n):
        if data[i][0] > data[j][0] and data[i][1] > data[j][1]:
            answer[j] += 1
        elif data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            answer[i] += 1
print(*answer)