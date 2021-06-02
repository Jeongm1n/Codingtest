import sys
import heapq

input = sys.stdin.readline

scoville = list(map(int, input().split()))
k = int(input())


def solution(scoville, k):
    scoville.sort()
    answer = 0
    while len(scoville) > 0:
        if scoville[0] >= k:
            return answer
        temp1 = heapq.heappop(scoville)
        if scoville:
            heapq.heappush(scoville, temp1 + (heapq.heappop(scoville) * 2))
            answer += 1
    return -1


print(solution(scoville, k))
