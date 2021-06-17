import sys

input = sys.stdin.readline

triangle = [list(map(int, input().split())) for _ in range(int(input()))]


def solution(triangle):
    triangle[1][0], triangle[1][1] = (
        triangle[0][0] + triangle[1][0],
        triangle[0][0] + triangle[1][1],
    )
    for i in range(2, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] = triangle[i - 1][-1] + triangle[i][j]
            else:
                triangle[i][j] = max(
                    triangle[i - 1][j - 1] + triangle[i][j],
                    triangle[i - 1][j] + triangle[i][j],
                )
    return max(triangle[-1])


print(solution(triangle))
