n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            if graph[a][b] == "Y" or (graph[a][k] == "Y" and graph[k][b] == "Y"):
                visited[a][b] = 1
answer = 0
for i in visited:
    answer = max(answer, i.count(1))
print(answer)
