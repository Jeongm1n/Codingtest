n = int(input())
h = list(map(int, input().split()))
flag = [0] * 1000001
answer = 0
for i in range(len(h)):
    if flag[h[i]] == 0:
        answer += 1
        flag[h[i] - 1] += 1
    else:
        flag[h[i]] -= 1
        flag[h[i] - 1] += 1
print(answer)
