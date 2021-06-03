import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    li = list(map(int, input().split()))
    graph.append(li)
    for j in range(n):
        if li[j] == 9:
            graph[i][j] = 2
            start = [i, j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    visited = [[0] * n for _ in range(n)]
    visited[i][j] = 1
    distance = [[0] * n for _ in range(n)]
    eat = []
    queue = deque()
    queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] <= graph[i][j]:
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
                if graph[nx][ny] < graph[i][j] and graph[nx][ny] != 0:
                    eat.append((nx, ny, distance[nx][ny]))
    if not eat:
        return -1, -1, -1
    eat.sort(key=lambda x: (x[2], x[0], x[1]))
    return eat[0][0], eat[0][1], eat[0][2]


exp = 0
answer = 0
while True:
    i, j = start[0], start[1]
    ex, ey, dist = bfs(i, j)
    if ex == -1:
        break
    graph[ex][ey] = graph[i][j]
    graph[i][j] = 0
    start = [ex, ey]
    exp += 1
    if exp == graph[ex][ey]:
        exp = 0
        graph[ex][ey] += 1
    answer += dist

print(answer)
