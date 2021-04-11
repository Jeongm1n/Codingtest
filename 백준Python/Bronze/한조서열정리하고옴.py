n = int(input())
data = list(map(int, input().split()))
maxValue = 0
for i in range(n-1):
    cnt = 0
    for j in range(i+1, n):
        if data[i] > data[j]:
            cnt += 1
        else:
            break
    if maxValue < cnt:
        maxValue = cnt
print(maxValue)