from collections import deque
a, b, n, m = map(int, input().split())

d = [-1, 1, a, b, -a, -b, a, b]

def bfs(s):
    queue = deque()
    queue.append(s)
    while queue:
        x = queue.popleft()
        for i in range(8):
            if i < 6:
                nx = x + d[i]
                if nx < 0 or nx > 100000:
                    continue
                if graph[nx] == 0:
                    graph[nx] = graph[x] + 1
                    queue.append(nx)
            else:
                nx = x * d[i]
                if nx < 0 or nx > 100000:
                    continue
                if graph[nx] == 0:
                    graph[nx] = graph[x] + 1
                    queue.append(nx)

graph = [0] * 100001
bfs(n)
print(graph[m])