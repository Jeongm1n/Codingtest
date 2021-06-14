import sys

input = sys.stdin.readline

brown, yellow = map(int, input().split())


def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            temp = yellow // i
            if i * 2 + temp * 2 + 4 == brown:
                return [temp + 2, i + 2]


print(solution(brown, yellow))
