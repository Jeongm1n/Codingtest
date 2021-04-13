from collections import deque
import sys
n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

queue = deque()
queue.append(1)
visited = [0]*(n+1)
answer = {}
while queue:
    p = queue.popleft()
    for i in tree[p]:
        if visited[i] == 0:
            visited[i] = 1
            answer[i] = p
            queue.append(i)

for i in range(2, n+1):
    print(answer[i])