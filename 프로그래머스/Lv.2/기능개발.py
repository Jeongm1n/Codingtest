import sys

input = sys.stdin.readline

progresses = list(map(int, input().split()))
speeds = list(map(int, input().split()))


def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        if progresses[0] >= 100:
            cnt = 0
            while len(progresses) > 0 and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
            answer.append(cnt)
    return answer


print(solution(progresses, speeds))
