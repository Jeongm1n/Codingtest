import sys

input = sys.stdin.readline

priorities = list(map(int, input().split()))
location = int(input())


def solution(priorities, location):
    priorities = [(priorities[x], x) for x in range(len(priorities))]
    answer = 0
    while True:
        if priorities[0][0] == max(priorities)[0] and priorities[0][1] == location:
            answer += 1
            break
        if priorities[0][0] < max(priorities)[0]:
            num, idx = priorities.pop(0)
            priorities.append((num, idx))
        else:
            answer += 1
            priorities.pop(0)
    return answer


print(solution(priorities, location))
