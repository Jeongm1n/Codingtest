import sys
import heapq

input = sys.stdin.readline

operations = [input().rstrip() for _ in range(int(input()))]


def solution(operations):
    q = []
    for s in operations:
        oper, num = s.split()[0], int(s.split()[1])
        if oper == "I":
            heapq.heappush(q, num)
        elif q and oper == "D":
            if num == 1:
                q.pop()
            else:
                heapq.heappop(q)
    if len(q) == 0:
        return [0, 0]
    return [max(q), min(q)]


print(solution(operations))
