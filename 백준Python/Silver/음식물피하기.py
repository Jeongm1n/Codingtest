import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [["."] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = "#"

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0


def bfs(x, y):
    global answer
    queue = deque()
    queue.append((x, y))
    size = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == "#":
                graph[nx][ny] = "."
                queue.append((nx, ny))
                size += 1
    answer = max(answer, size)


for i in range(n):
    for j in range(m):
        if graph[i][j] == "#":
            graph[i][j] = "."
            bfs(i, j)

print(answer)
