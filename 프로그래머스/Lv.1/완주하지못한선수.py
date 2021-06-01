import sys

input = sys.stdin.readline
participant = list(map(str, input().split()))
completion = list(map(str, input().split()))


def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]
    return participant[-1]


print(solution(participant, completion))
