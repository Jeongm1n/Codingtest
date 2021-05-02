import sys
x, y = map(int, sys.stdin.readline().split())
z = y*100//x
start = 0
end = x
if z >= 99:
    print(-1)
else:
    answer = 0
    while start <= end:
        mid = (start+end)//2
        if 100*(y+mid)//(x+mid) > z:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    print(answer)