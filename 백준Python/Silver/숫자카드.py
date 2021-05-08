# import sys
# n = int(sys.stdin.readline())
# a = set(list(map(int, sys.stdin.readline().split())))
# m = int(sys.stdin.readline())
# b = list(map(int, sys.stdin.readline().split()))
# for i in b:
#     if i in a:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')
import sys
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

def binary_search(array, t, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == t:
            return mid
        elif array[mid] > t:
            end = mid - 1
        else:
            start = mid + 1
    return None

answer = 0
for t in target:
    answer = binary_search(array, t, 0, n-1)
    if answer == None:
        print(0, end=' ')
    else:
        print(1, end=' ')