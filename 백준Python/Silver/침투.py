import sys
from collections import deque
m, n = map(int, sys.stdin.readline().split())
graph = []
for _ in range(m):
    graph.append(list(sys.stdin.readline()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    graph[x][y] == '2'
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny <0 or ny >= n or nx >= m:
                continue
            if graph[nx][ny] == '0':
                graph[nx][ny] = '2'
                queue.append([nx, ny])

for i in range(n):
    if graph[0][i] == '0':
        bfs(0, i)

print('YES' if '2' in graph[-1] else 'NO')