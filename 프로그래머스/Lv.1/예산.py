import sys

input = sys.stdin.readline

d = list(map(int, input().split()))
budget = int(input())


def solution(d, budget):
    d.sort()
    temp, answer = 0, 0
    for i in range(len(d)):
        temp += d[i]
        if temp > budget:
            break
        answer += 1
    return answer


print(solution(d, budget))
