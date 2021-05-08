n = int(input())
array = [float(input()) for _ in range(n)]
d = [0] * 10001
d[0], d[1] = array[0], max(array[1], array[0] * array[1])
for i in range(2, n):
    d[i] = max(array[i], d[i - 1] * array[i])
print(format(max(d), ".3f"))
