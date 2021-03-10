import heapq
n = int(input())
card = []
for _ in range(n):
    heapq.heappush(card, int(input()))
if len(card) == 1:
    print(0)
else:
    answer = 0
    while len(card) > 1:
        temp_1 = heapq.heappop(card)
        temp_2 = heapq.heappop(card)
        answer += (temp_1 + temp_2)
        heapq.heappush(card, (temp_1+temp_2))
    print(answer)