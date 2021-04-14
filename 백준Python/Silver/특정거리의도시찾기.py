import sys
from collections import deque
n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
result = [-1] * (n+1)
result[x] = 0
queue = deque()
queue.append(x)
while queue:
    d = queue.popleft()
    for i in graph[d]:
        if result[i] == -1:
            result[i] = result[d] + 1
            queue.append(i)
for i in range(n+1):
    if result[i] == k:
        print(i)
if k not in result:
    print(-1)