import math

n = str(math.factorial(int(input())))
answer = 0
for i in range(len(n) - 1, -1, -1):
    if n[i] != "0":
        break
    answer += 1

print(answer)
