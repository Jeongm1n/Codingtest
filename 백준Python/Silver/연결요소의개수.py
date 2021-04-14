import sys
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0]*(n+1)

def bfs(v):
    queue = [v]
    while queue:
        n = queue.pop(0)
        for i in graph[n]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)

answer = 0
for i in range(1, n+1):
    if visited[i] == 0:
        bfs(i)
        answer += 1
print(answer)