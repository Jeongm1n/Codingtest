import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append((a, ""))
    while queue:
        num, result = queue.popleft()
        dn = (num * 2) % 10000
        if dn == b:
            return result + "D"
        elif visited[dn] == 0:
            visited[dn] = 1
            queue.append((dn, result + "D"))
        sn = num - 1 if num != 0 else 9999
        if sn == b:
            return result + "S"
        elif visited[sn] == 0:
            visited[sn] = 1
            queue.append((sn, result + "S"))
        ln = int(num % 1000 * 10 + num / 1000)
        if ln == b:
            return result + "L"
        elif visited[ln] == 0:
            visited[ln] = 1
            queue.append((ln, result + "L"))
        rn = int(num % 10 * 1000 + num // 10)
        if rn == b:
            return result + "R"
        elif visited[rn] == 0:
            visited[rn] = 1
            queue.append((rn, result + "R"))


for _ in range(int(input())):
    a, b = map(int, input().split())
    visited = [0] * 10000
    print(bfs())
