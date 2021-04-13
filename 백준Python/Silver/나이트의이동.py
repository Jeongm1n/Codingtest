from collections import deque
import sys
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(cx, cy, gx, gy):
    q = deque()
    q.append([cx, cy])
    s[cx][cy] = 1
    while q:
        x, y = q.popleft()
        if x == gx and y == gy:
            print(s[gx][gy]-1)
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if s[nx][ny] == 0:
                q.append([nx, ny])
                s[nx][ny] = s[x][y] + 1

t = int(sys.stdin.readline())
for _ in range(t):
    l = int(sys.stdin.readline())
    cx, cy = map(int, sys.stdin.readline().split())
    gx, gy = map(int, sys.stdin.readline().split())
    s = [[0]*l for _ in range(l)]
    bfs(cx, cy, gx, gy)