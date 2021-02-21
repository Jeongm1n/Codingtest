import heapq
def solution(scoville, K):
    scoville.sort()
    answer = 0
    while len(scoville) > 0:
        if scoville[0] >= K:
            return answer
        a = heapq.heappop(scoville)
        if scoville:
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a+(b*2))
        answer += 1
    return -1
scoville = list(map(int, input().split()))
K = int(input())
print(solution(scoville, K))