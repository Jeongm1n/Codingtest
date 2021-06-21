fibo = [0, 1]
for i in range(2, 50):
    fibo.append(fibo[i - 2] + fibo[i - 1])

for _ in range(int(input())):
    n = int(input())
    answer = []
    while n:
        for i in range(50):
            if fibo[i] <= n:
                t = fibo[i]

        n = n - t
        answer.append(t)
    answer.sort()
    print(*answer)
