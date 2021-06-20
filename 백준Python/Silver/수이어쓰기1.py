import sys

input = sys.stdin.readline

n = int(input())
n = str(n)

answer = 0
for i in range(len(n) - 1):
    answer += 9 * (i + 1) * 10 ** i

answer += (int(n) - (10 ** (len(n) - 1)) + 1) * len(n)

print(answer)
