from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
answer = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= len(graph[0]):
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt += 1
                queue.append((nx, ny))
    answer.append(cnt + 1)


total = 0
for i in range(n):
    for j in range(len(graph[0])):
        if graph[i][j] == 1:
            total += 1
            bfs(i, j)
print(total)
answer.sort()
for cnt in answer:
    print(cnt)
