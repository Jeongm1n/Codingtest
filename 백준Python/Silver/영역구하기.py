from collections import deque

m, n, k = map(int, input().split())
graph = [[0] * n for i in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

l = []

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            graph[k][j] = 1


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    graph[x][y] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    cnt += 1
                    queue.append([nx, ny])
    l.append(cnt)


for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            bfs(i, j)

print(len(l))
l.sort()
print(*l)
