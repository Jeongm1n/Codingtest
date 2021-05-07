def factorial(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num


for _ in range(int(input())):
    n, m = map(int, input().split())
    bridge = factorial(m) // (factorial(n) * factorial(m - n))
    print(bridge)
