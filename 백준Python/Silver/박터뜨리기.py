n, k = map(int, input().split())
minimum = k * (k + 1) // 2
if minimum > n:
    print(-1)

elif (n - minimum) % k == 0:
    print(k - 1)
else:
    print(k)
