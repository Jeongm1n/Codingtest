n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
tempA = sorted(a)
tempB = sorted(b, reverse=True)
answer = 0
for i in range(n):
    answer += (tempA[i]*tempB[i])
print(answer)