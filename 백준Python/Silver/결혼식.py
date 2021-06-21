import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]


def search(start):
    visited = [0] * (n + 1)
    visited[start] = 1
    queue = deque()
    queue.append((start, 0))
    answer = 0
    while queue:
        x, cnt = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0 and cnt < 2:
                visited[i] = 1
                queue.append((i, cnt + 1))
                answer += 1
    return answer


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(search(1))
