n = int(input())
arr = list(map(int, input().split()))
d = [0] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1

print(max(d))
