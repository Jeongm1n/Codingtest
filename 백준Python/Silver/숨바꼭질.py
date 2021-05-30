from collections import deque

n, k = map(int, input().split())
graph = [0] * 100001

dx = [-1, 1, 2]


def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft()
        if x == k:
            print(graph[x])
            break
        for i in range(3):
            if i == 2:
                nx = x * dx[i]
            else:
                nx = x + dx[i]
            if 0 <= nx < 100001 and graph[nx] == 0:
                graph[nx] = graph[x] + 1
                queue.append(nx)


bfs(n)
