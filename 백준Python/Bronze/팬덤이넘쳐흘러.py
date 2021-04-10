n = int(input())
data = []
for _ in range(n):
    x, y = map(int, input().split())
    data.append([x, y])
first = sorted(data, key=lambda x: x[0])
second = sorted(data, key=lambda x: x[1])

answer = first[-1][0] - second[0][1]

if answer <= 0:
    print(0)
else:
    print(answer)