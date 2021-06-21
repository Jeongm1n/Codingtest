import sys
import heapq

q = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if not q and num == 0:
        print(0)
    else:
        if num == 0:
            print(-heapq.heappop(q))
        else:
            heapq.heappush(q, -num)
