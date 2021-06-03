import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, c, colorList):
    queue = deque()
    queue.append((x, y))
    colorList[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < n) and colorList[nx][ny] != 0:
                if colorList[nx][ny] == c:
                    queue.append((nx, ny))
                    colorList[nx][ny] = 0


graph = [list(map(str, input().rstrip())) for _ in range(n)]
copy = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == "R" or graph[i][j] == "G":
            copy[i][j] = 1
        else:
            copy[i][j] = 2

answer1 = 0
answer2 = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            bfs(i, j, graph[i][j], graph)
            answer1 += 1
        if copy[i][j] != 0:
            bfs(i, j, copy[i][j], copy)
            answer2 += 1

print(answer1, answer2)
