t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    answer = 0
    for i in range(2, n):
        answer = max(answer, abs(arr[i]-arr[i-2]))
    print(answer)