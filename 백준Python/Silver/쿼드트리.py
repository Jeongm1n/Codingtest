import sys

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]


def quadtree(n, x, y):
    check = data[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != data[i][j]:
                print("(", end="")
                quadtree(n // 2, x, y)
                quadtree(n // 2, x, y + n // 2)
                quadtree(n // 2, x + n // 2, y)
                quadtree(n // 2, x + n // 2, y + n // 2)
                print(")", end="")
                return

    if check == 0:
        print("0", end="")

    else:
        print("1", end="")


quadtree(n, 0, 0)
