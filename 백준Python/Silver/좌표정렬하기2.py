import sys
n = int(sys.stdin.readline())
data = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    data.append([x, y])
answer = sorted(data, key=lambda x: (x[1], x[0]))
for i in range(n):
    print(answer[i][0], answer[i][1])