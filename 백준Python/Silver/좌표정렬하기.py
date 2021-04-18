n = int(input())
data = []
for _ in range(n):
    x, y = map(int, input().split())
    data.append([x, y])
answer = sorted(data, key=lambda x: (x[0], x[1]))
for i in range(n):
    print(answer[i][0], answer[i][1])