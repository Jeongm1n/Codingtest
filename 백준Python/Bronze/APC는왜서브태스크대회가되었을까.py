n, l, k = map(int, input().split())
score, cnt = 0, 0
problem = []
for _ in range(n):
    sub1, sub2 = map(int, input().split())
    if sub2 <= l:
        cnt += 1
        score += 140
    else:
        problem.append([sub1, sub2])

if cnt > k:
    score -= (140*(cnt-k))
else:
    for i in range(len(problem)):
        if problem[i][0] <= l:
            cnt += 1
            score += 100
        if cnt == k:
            break
print(score)