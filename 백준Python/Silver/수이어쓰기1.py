import sys

input = sys.stdin.readline

n = int(input())
n = str(n)

temp = 0
for i in range(len(n) - 1):
    temp += 9 * (i + 1) * 10 ** i

temp += (int(n) - (10 ** (len(n) - 1)) + 1) * len(n)

print(temp)
