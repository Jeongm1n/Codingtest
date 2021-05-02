import sys
k, n = map(int, sys.stdin.readline().split())
data = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1, max(data)
while start <= end:
    mid = (start+end)//2 # 중간위치
    lines = 0 # 랜선 수
    for line in data:
        lines += line//mid # 분할 된 랜선 개수
    if lines >= n: # 랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1
print(end)