import sys

input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
commands = [list(map(int, input().split())) for _ in range(n)]


def solution(array, commands):
    answer = []
    for i in commands:
        temp = array[i[0] - 1 : i[1]]
        temp.sort()
        answer.append(temp[i[2] - 1])
    return answer


print(solution(array, commands))
