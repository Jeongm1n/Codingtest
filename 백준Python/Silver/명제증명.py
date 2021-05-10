INF = int(1e9)
n = int(input())
graph = [[INF] * (52) for _ in range(52)]
for _ in range(n):
    answer = input().split()
    dx, dy = 0, 0
    if "A" <= answer[0] <= "Z":
        dx = ord(answer[0]) - 65
    else:
        dx = ord(answer[0]) - 71
    if "A" <= answer[2] <= "Z":
        dy = ord(answer[2]) - 65
    else:
        dy = ord(answer[2]) - 71
    graph[dx][dy] = 1

for k in range(52):
    for a in range(52):
        for b in range(52):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
cnt = 0
for i in range(52):
    for j in range(52):
        if i == j:
            continue
        if graph[i][j] != INF:
            cnt += 1

print(cnt)
for i in range(52):
    for j in range(52):
        ret = ""
        if i == j:
            continue
        if graph[i][j] == INF:
            continue
        if 0 <= i < 26:
            ret += chr(i + 65)
        else:
            ret += chr(i + 71)
        ret += " => "
        if 0 <= j < 26:
            ret += chr(j + 65)
        else:
            ret += chr(j + 71)
        print(ret)
