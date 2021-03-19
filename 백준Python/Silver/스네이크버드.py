n, l = map(int, input().split())
h = list(map(int, input().split()))
h.sort()
answer = l
for i in range(n):
    if h[i] <= answer:
        answer += 1
print(answer)