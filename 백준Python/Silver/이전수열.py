import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

k = -1
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        k = i

if k == -1:
    print(-1)
else:
    for i in range(k + 1, len(arr)):
        if arr[i] < arr[k]:
            m = i

    arr[k], arr[m] = arr[m], arr[k]

    temp = arr[k + 1 :]
    temp.sort(reverse=True)
    answer = arr[: k + 1] + temp

    for num in answer:
        print(num, end=" ")
