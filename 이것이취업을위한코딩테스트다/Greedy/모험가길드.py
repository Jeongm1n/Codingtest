n = int(input())
data = list(map(int, input().split()))
answer, cnt = 0
data.sort()
for element in data:
    cnt += 1
    if cnt == element:
        answer += 1
        cnt = 0
print(answer)