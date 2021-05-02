# import sys
# n = int(sys.stdin.readline())
# a = set(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# b = list(map(int, sys.stdin.readline().split()))
# for num in b:
#     sys.stdout.write('1\n') if num in a else sys.stdout.write('0\n')
n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
target = list(map(int, input().split()))

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
        print(0)
    else:
        print(1)