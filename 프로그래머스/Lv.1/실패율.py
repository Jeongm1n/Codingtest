import sys

input = sys.stdin.readline

n = int(input())
stages = list(map(int, input().split()))


def solution(n, stages):
    answer = {}
    length = len(stages)
    for stage in range(1, n + 1):
        if length != 0:
            cnt = stages.count(stage)
            answer[stage] = cnt / length
            length -= cnt
        else:
            answer[stage] = 0
    return sorted(answer, key=lambda x: answer[x], reverse=True)


print(solution(n, stages))
