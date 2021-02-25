n, k = map(int, input().split())
data = []
start = -1
k -= 1
for _ in range(n):
    i = int(input())
    if start == -1:
        start = i
        continue
    data.append(i-start)
    start = i
data.sort()
answer = 1
for i in range(len(data)):
    if k:
        answer += 1
        data.pop()
        k -= 1
    else:
        answer += data.pop()
print(answer)