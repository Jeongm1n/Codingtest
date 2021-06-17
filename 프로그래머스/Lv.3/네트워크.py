import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
compters = [list(map(int, input().split())) for _ in range(n)]


def bfs(n, computers, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        x = queue.popleft()
        for i in range(len(computers[x])):
            if i == x:
                continue
            if visited[i] == False and computers[x][i] == 1:
                visited[i] = True
                queue.append(i)


def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if visited[i] == False:
            bfs(n, computers, i, visited)
            answer += 1

    return answer


print(solution(n, compters))
