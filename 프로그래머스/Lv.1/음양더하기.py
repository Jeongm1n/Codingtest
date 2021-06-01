import sys

input = sys.stdin.readline
absolutes = list(map(int, input().split()))
signs = list(map(int, input().split()))


def solution(absolutes, signs):
    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] *= -1
    return sum(absolutes)


print(solution(absolutes, signs))
