e, s, m = map(int, input().split())
answer = 0
while 1:
    if e == 1 and s == 1 and m == 1:
        break
    answer += 1
    e -= 1
    s -= 1
    m -= 1
    if e == 0:
        e = 15
    if s == 0:
        s = 28
    if m == 0:
        m = 19
print(answer + 1)
