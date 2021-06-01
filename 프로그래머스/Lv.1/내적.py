import sys

input = sys.stdin.readline
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer


print(solution(a, b))
