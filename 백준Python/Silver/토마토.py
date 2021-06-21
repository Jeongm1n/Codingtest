from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i, j))

bfs()

isTrue = False
answer = -2
for i in graph:
    for j in i:
        if j == 0:
            isTrue = True
        answer = max(answer, j)
if isTrue == True:
    print(-1)
else:
    print(answer - 1)
