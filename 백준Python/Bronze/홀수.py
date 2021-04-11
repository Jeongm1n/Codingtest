sumAnswer = 0
minAnswer = 101
for _ in range(7):
    n = int(input())
    if n%2 == 1:
        sumAnswer += n
        if minAnswer > n:
            minAnswer = n
if sumAnswer == 0:
    print(-1)
else:
    print(sumAnswer)
    print(minAnswer)