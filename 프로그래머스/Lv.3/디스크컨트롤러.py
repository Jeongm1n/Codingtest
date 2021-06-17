import sys
import heapq

input = sys.stdin.readline

jobs = [list(map(int, input().split())) for _ in range(int(input()))]


def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    q = []

    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(q, (job[1], job[0]))
        if q:
            current = heapq.heappop(q)
            start = now
            now += current[0]
            answer += now - current[1]
            i += 1
        else:
            now += 1

    return answer // len(jobs)


print(solution(jobs))
