n, m = map(int, input().split())
k = list(map(int, input().split()))
answer = 0
while len(k) > 1:
    answer += (len(k)-k.count(k[0]))
    k.pop(0)
print(answer)