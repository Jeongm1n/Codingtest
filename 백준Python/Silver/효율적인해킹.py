import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
trust = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    trust[b].append(a)

def bfs(s):
    cnt = 0
    queue = deque()
    queue.append(s)
    visited = [0] * (n+1)
    visited[s] = 1
    while queue:
        x = queue.popleft()
        cnt += 1
        for i in trust[x]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
    return cnt

maxValue = 0
result = []
for i in range(1, n+1):
    if trust[i]:
        tmp = bfs(i)
        if maxValue <= tmp:
            if maxValue < tmp:
                result = []
            result.append(i)
            maxValue = tmp
print(*result)