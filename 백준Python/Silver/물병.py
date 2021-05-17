n, k = map(int, input().split())
temp = n
while bin(n).count("1") > k:
    n += n & -n
print(n - temp)
