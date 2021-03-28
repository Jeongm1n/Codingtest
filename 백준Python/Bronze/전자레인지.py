t = int(input())
a, b, c = 300, 60, 10
answer = [0, 0, 0]
if t%10 != 0:
    print(-1)
else:
    if t//300 != 0:
        answer[0] += t//300
        t = t%300
    if t//60 != 0:
        answer[1] += t//60
        t = t%60
    if t//10 != 0:
        answer[2] += t//10
    print(*answer)