import sys

input = sys.stdin.readline

citations = list(map(int, input().split()))


def solution(citations):
    citations.sort()
    for i in range(len(citations)):
        if len(citations) - i <= citations[i]:
            return len(citations) - i
    return 0


print(solution(citations))
