n = int(input())
array = list(map(int, input().split()))
d1, d2 = [1] * (n + 1), [1] * (n + 1)
for i in range(1, n):
    if array[i] <= array[i - 1]:
        d1[i] = d1[i - 1] + 1
    if array[i] >= array[i - 1]:
        d2[i] = d2[i - 1] + 1
print(max(max(d1), max(d2)))
