n = int(input())
arr = list(map(int, input().split()))
answer = 0
for i in range(n):
    cnt = 0
    for j in range(1, arr[i]+1):
        if arr[i]%j == 0:
            cnt += 1
    if cnt == 2:
        answer += 1
print(answer)