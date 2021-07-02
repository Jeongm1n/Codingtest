import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(str, input().rstrip())))

distance = [[-1] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    distance[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1:
                if graph[nx][ny] == "1" or graph[nx][ny] == "#":
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
                elif graph[nx][ny] == "0":
                    distance[nx][ny] = distance[x][y]
                    queue.appendleft((nx, ny))


bfs(x1 - 1, y1 - 1)

print(distance[x2 - 1][y2 - 1])
