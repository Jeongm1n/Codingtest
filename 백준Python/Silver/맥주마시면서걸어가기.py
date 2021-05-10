from collections import deque


def bfs(startX, startY):
    queue, visited = deque(), []
    queue.append([startX, startY])
    visited.append([startX, startY])
    while queue:
        x, y = queue.popleft()
        if x == endX and y == endY:
            print("happy")
            return
        for nx, ny in graph:
            if [nx, ny] not in visited:
                dist = abs(nx - x) + abs(ny - y)
                if dist <= 1000:
                    queue.append([nx, ny])
                    visited.append([nx, ny])
    print("sad")
    return


for _ in range(int(input())):
    n = int(input())
    startX, startY = map(int, input().split())
    graph = []
    for _ in range(n):
        x, y = map(int, input().split())
        graph.append([x, y])
    endX, endY = map(int, input().split())
    graph.append([endX, endY])
    bfs(startX, startY)
