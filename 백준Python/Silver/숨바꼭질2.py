import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [-1] * (n + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            if distance[i] == -1:
                distance[i] = dist + 1
                heapq.heappush(q, (distance[i], i))


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dijkstra(1)

print(distance.index(max(distance)), max(distance), distance.count(max(distance)))
