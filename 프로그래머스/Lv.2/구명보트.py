import sys

input = sys.stdin.readline

limit = int(input())
people = list(map(int, input().split()))


def solution(people, limit):
    people.sort()
    answer = 0
    i, j = 0, len(people) - 1
    while i <= j:
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return answer


print(solution(people, limit))
