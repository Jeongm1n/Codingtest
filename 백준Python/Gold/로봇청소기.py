import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[r][c] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turnLeft():
    global d
    d -= 1
    if d == -1:
        d = 3


turnTime = 0
answer = 1
while True:
    turnLeft()
    nx = r + dx[d]
    ny = c + dy[d]
    if visited[nx][ny] == 0 and graph[nx][ny] == 0:
        visited[nx][ny] = 1
        r, c = nx, ny
        answer += 1
        turnTime = 0
        continue
    else:
        turnTime += 1
    if turnTime == 4:
        nx = r - dx[d]
        ny = c - dy[d]
        if graph[nx][ny] == 0:
            r, c = nx, ny
        else:
            break
        turnTime = 0

print(answer)
