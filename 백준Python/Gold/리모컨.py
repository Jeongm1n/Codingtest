import sys

input = sys.stdin.readline
enable = {str(i) for i in range(10)}
n = int(input())
m = int(input())
if m != 0:
    enable -= set(map(str, input().split()))

answer = abs(100 - n)

for num in range(1000001):
    num = str(num)
    for j in range(len(num)):
        if num[j] not in enable:
            break
        elif j == len(num) - 1:
            answer = min(answer, abs(n - int(num)) + len(num))

print(answer)
