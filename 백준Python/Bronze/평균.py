n = int(input())
score = list(map(int, input().split()))
m = max(score)
fake = 0
for i in range(n):
    fake += score[i]/m*100
print(fake/n)