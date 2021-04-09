m = int(input())
n = int(input())
sumAnswer = 0
minAnswer = 10001
while m <= n:
    if pow(m, 0.5)-int(pow(m, 0.5)) == 0:
        sumAnswer += m
        if minAnswer == 10001:
            minAnswer = m
    m += 1
if sumAnswer == 0:
    print(-1)
else:
    print(sumAnswer)
    print(minAnswer)