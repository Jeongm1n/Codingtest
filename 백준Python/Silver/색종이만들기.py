import sys

n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
white, blue = 0, 0


def divide(n, x, y):
    global white, blue
    check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                divide(n // 2, x, y)
                divide(n // 2, x, y + n // 2)
                divide(n // 2, x + n // 2, y)
                divide(n // 2, x + n // 2, y + n // 2)
                return
    if check == 0:
        white += 1
    else:
        blue += 1


divide(n, 0, 0)
print(white)
print(blue)
