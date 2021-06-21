from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [start]
    distance = [0] * (n + 1)
    while queue:
        d = queue.popleft()
        for i in graph[d]:
            if i not in visited:
                distance[i] = distance[d] + 1
                visited.append(i)
                queue.append(i)
    return sum(distance)


answer = []
for i in range(1, n + 1):
    answer.append(bfs(i))
print(answer.index(min(answer)) + 1)
