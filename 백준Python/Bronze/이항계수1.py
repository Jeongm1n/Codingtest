import math
n, k = map(int, input().split())
if k < 0:
    print(0)
elif k > n:
    print(0)
else:
    print(int((math.factorial(n))/(math.factorial(k)*math.factorial(n-k))))