import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

size = 0
answer_size = 0
cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global size, answer_size
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                size += 1
                graph[nx][ny] = 0
                queue.append((nx, ny))
    answer_size = max(size, answer_size)
    size = 0


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = 0
            size = 1
            cnt += 1
            bfs(i, j)

print(cnt)
print(answer_size)
