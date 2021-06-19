n, d = map(int, input().split())
graph = [[] for _ in range(10001)]
for _ in range(n):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
distance = [i for i in range(d + 1)]

for i in range(d + 1):
    if i != 0:
        distance[i] = min(distance[i], distance[i - 1] + 1)
    for w, e in graph[i]:
        if e <= d and distance[e] > distance[i] + w:
            distance[e] = distance[i] + w
print(distance[d])
