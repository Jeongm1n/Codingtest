import sys
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
limit = int(sys.stdin.readline())

if limit >= sum(array):
    print(max(array))
else:
    array.sort()
    start = 0
    end = array[-1]
    while start <= end:
        mid = (start+end)//2
        total = 0
        for i in array:
            if mid > i:
                total += i
            else:
                total += mid
        if total > limit:
            end = mid - 1
        else:
            start = mid + 1
    print(end)