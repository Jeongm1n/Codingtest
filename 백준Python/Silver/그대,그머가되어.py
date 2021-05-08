import heapq

INF = int(1e9)
a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
distance = [INF] * (n + 1)


def dijkstra(start, end):
    q = []
    heapq.heappush(q, start)
    distance[start] = 0
    while q:
        now = heapq.heappop(q)
        for i in graph[now]:
            cost = distance[now] + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, i)
    if distance[end] != INF:
        print(distance[end])
    else:
        print(-1)


dijkstra(a, b)
