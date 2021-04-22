from collections import deque
n = int(input())
a, b = map(int, input().split())
m = int(input())
relation = [[] for _ in range(n+1)]
result = [0] * (n+1)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited = [0] * (n+1)
    visited[v] = 1
    while queue:
        d = queue.popleft()
        for i in relation[d]:
            if visited[i] == 0:
                visited[i] = 1
                result[i] = result[d] + 1
                queue.append(i)

for _ in range(m):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)
bfs(a)
print(result[b] if result[b] != 0 else -1)