import sys

n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
minusOne, zero, one = 0, 0, 0


def divide(n, x, y):
    global minusOne, zero, one

    num = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if num != paper[i][j]:
                for k in range(3):
                    for l in range(3):
                        divide(n // 3, x + k * n // 3, y + l * n // 3)
                return
    if num == -1:
        minusOne += 1
    elif num == 0:
        zero += 1
    else:
        one += 1


divide(n, 0, 0)
print(minusOne)
print(zero)
print(one)
