import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = []
    answer = 0
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        data.append([x, y])
    data = sorted(data, key=lambda x: x[0])
    cnt = 1
    min_value = data[0][1]
    for i in range(1, n):
        if min_value > data[i][1]:
            min_value = data[i][1]
            cnt += 1
    print(cnt)