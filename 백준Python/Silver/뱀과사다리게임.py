import sys
from collections import deque

distance = [-1] * 101


def bfs(x):
    queue = deque()
    queue.append(x)
    distance[x] = 0
    while queue:
        x = queue.popleft()
        for i in range(1, 7):
            nx = x + i
            if nx > 100:
                continue
            if graph[nx]:
                if (
                    distance[graph[nx][0]] == -1
                    or distance[graph[nx][0]] > distance[x] + 1
                ):
                    distance[graph[nx][0]] = distance[x] + 1
                    queue.append(graph[nx][0])
            else:
                if distance[nx] == -1 or distance[nx] > distance[x] + 1:
                    distance[nx] = distance[x] + 1
                    queue.append(nx)


graph = [[] for _ in range(101)]
n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
bfs(1)
print(distance[-1])
