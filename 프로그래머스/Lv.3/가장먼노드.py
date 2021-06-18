import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
vertex = [list(map(int, input().split())) for _ in range(int(input()))]


def getDistance(start, graph, distance):
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if i == 1:
                continue
            if distance[i] == 0:
                distance[i] += distance[x] + 1
                queue.append(i)
    return distance


def solution(n, vertex):
    graph = [[] for _ in range(n + 1)]
    distance = [0] * (n + 1)

    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    temp = getDistance(1, graph, distance)

    return temp.count(max(temp))


print(solution(n, vertex))
