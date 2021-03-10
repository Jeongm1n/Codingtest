import sys
n, m = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(height)
while start <= end:
    mid = (start+end)//2
    temp = 0
    for element in height:
        if element >= mid:
            temp += (element-mid)
    if temp >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)