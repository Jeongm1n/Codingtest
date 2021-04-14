import sys
from collections import deque
r, c = map(int, sys.stdin.readline().split())
k, v = 0, 0
graph = []
visited = [[0]*c for _ in range(r)]
for _ in range(r):
    line = list(sys.stdin.readline())
    graph.append(line)
    for i in range(c):
        if line[i] == 'k':
            k += 1
        elif line[i] == 'v':
            v += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global k, v
    tk, tv = 0, 0
    if graph[x][y] == 'k':
        tk += 1
    elif graph[x][y] == 'v':
        tv += 1
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] != '#':
                if graph[nx][ny] == 'k':
                    tk += 1
                elif graph[nx][ny] == 'v':
                    tv += 1
                visited[nx][ny] = 1
                queue.append([nx, ny])
    if tk > tv:
        v -= tv
    else:
        k -= tk


for i in range(r):
    for j in range(c):
        if (graph[i][j] == 'k' or graph[i][j] == 'v') and visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i, j)
print(k, v)