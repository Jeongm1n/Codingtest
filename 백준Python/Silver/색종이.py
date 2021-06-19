import sys

input = sys.stdin.readline

paper = [[0] * 101 for _ in range(101)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

answer = 0
for row in paper:
    answer += row.count(1)

print(answer)
