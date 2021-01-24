def solution(scoville, K):
    import heapq
    scoville.sort()
    answer = 0
    while len(scoville) >0:
        if scoville[0] >= K:
            return answer
        a= heapq.heappop(scoville)
        if scoville != []:
            b =heapq.heappop(scoville)
            heapq.heappush(scoville,a + (b *2))
        answer +=1    
    return -1

scoville = [2,4,8]
K = 7
print(solution(scoville, K))