import sys

input = sys.stdin.readline
lottos = list(map(int, input().split()))
win_nums = list(map(int, input().split()))


def solution(lottos, win_nums):
    if sum(lottos) == 0:
        return [1, 6]
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
    zero = lottos.count(0)
    if cnt == 0 and zero == 0:
        return [6, 6]
    return [7 - (cnt + zero), 7 - cnt]


print(solution(lottos, win_nums))
