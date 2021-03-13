n, k = map(int, input().split())
arr = []
for i in range(n):
    coin = int(input())
    arr.append(coin)
answer = 0
for i in range(n-1, -1, -1):
    if k // arr[i] >= 1:
        answer += (k//arr[i])
        k %= arr[i]
print(answer)