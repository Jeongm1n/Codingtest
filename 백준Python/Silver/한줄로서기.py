import sys

input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))

answer = [0] * n

for i in range(1, n + 1):
    temp = line[i - 1]
    cnt = 0
    for j in range(n):
        if temp == cnt and answer[j] == 0:
            answer[j] = i
            break
        elif answer[j] == 0:
            cnt += 1

print(*answer)
