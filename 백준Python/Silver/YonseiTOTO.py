import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
temp = []
for _ in range(n):
    p, l = map(int, input().split())
    mileages = list(map(int, input().split()))
    heapq.heapify(mileages)
    num = l - p
    if num > 0:
        heapq.heappush(temp, 1)
    else:
        for i in range(abs(num)):
            heapq.heappop(mileages)
        heapq.heappush(temp, mileages[0])

answer = 0
while temp:
    mileage = heapq.heappop(temp)
    if m - mileage >= 0:
        answer += 1
        m -= mileage
    else:
        break
print(answer)
