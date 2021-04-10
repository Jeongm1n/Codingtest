answer = 0
maxCnt = 0
for _ in range(4):
    x, y = map(int, input().split())
    answer -= x
    answer += y
    if maxCnt < answer:
        maxCnt = answer
print(maxCnt)