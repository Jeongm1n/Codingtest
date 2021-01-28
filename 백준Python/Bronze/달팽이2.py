m, n = map(int, input().split())
a, b = n, m
answer = 0

while 1:
    if a == 1 or b == 1:
        answer = 1
        break
    m -= 1
    if m == 0:
        break
    answer += 1
    
    n -= 1
    if n == 0:
        break
    answer += 1

    
print(answer)