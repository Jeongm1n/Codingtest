from collections import deque
import sys

m, n, h = map(int, sys.stdin.readline().split())

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and graph[nz][nx][ny] == 0:
                queue.append([nx, ny, nz])
                graph[nz][nx][ny] = graph[z][x][y] + 1


graph = [[] for _ in range(h)]
queue = deque()
isTrue = False
for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, sys.stdin.readline().split())))

for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                queue.append([x, y, z])

bfs()

maxValue = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 0:
                isTrue = True
                break
            maxValue = max(maxValue, graph[z][x][y])

if isTrue == True:
    print(-1)
else:
    print(maxValue - 1)
