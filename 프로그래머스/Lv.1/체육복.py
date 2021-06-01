import sys

input = sys.stdin.readline
n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))


def solution(n, lost, reserve):
    setLost = set(lost) - set(reserve)
    setReserve = set(reserve) - set(lost)
    for i in setReserve:
        if i - 1 in setLost:
            setLost.remove(i - 1)
        elif i + 1 in setLost:
            setLost.remove(i + 1)
    return n - len(setLost)


print(solution(n, lost, reserve))
