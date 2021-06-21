n, k = map(int, input().split())
child = list(map(int, input().split()))
temp = []
for i in range(n - 1):
    temp.append(child[i + 1] - child[i])
temp.sort()
answer = 0
for i in range(n - k):
    answer += temp[i]
print(answer)
