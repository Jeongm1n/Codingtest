import heapq
import sys

n = int(sys.stdin.readline())
q = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if not q and num == 0:
        print(0)
    else:
        if num != 0:
            heapq.heappush(q, num)
        else:
            print(heapq.heappop(q))
