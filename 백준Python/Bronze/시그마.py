a, b = map(int, input().split())
answer = 0
if a > b:
    a, b = b, a
print((a+b) * (b-a+1) // 2)