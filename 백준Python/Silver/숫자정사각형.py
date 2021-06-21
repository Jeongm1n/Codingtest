import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(str, input().rstrip())) for _ in range(n)]
temp = min(n, m)
answer = 0
for i in range(n):
    for j in range(m):
        for k in range(temp):
            if i + k < n and j + k < m:
                if (
                    arr[i][j] == arr[i][j + k]
                    and arr[i][j] == arr[i + k][j]
                    and arr[i][j] == arr[i + k][j + k]
                ):
                    answer = max(answer, (k + 1) ** 2)
print(answer)
