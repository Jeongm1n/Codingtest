import sys

n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(n)]
data.sort(reverse=True)
answer, k = 0, 2
for i in range(n):
    if i == k:
        k += 3
        continue
    answer += data[i]
print(answer)
