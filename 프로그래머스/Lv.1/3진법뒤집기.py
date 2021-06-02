import sys

input = sys.stdin.readline

n = int(input())


def solution(n):
    temp = []
    answer = 0
    if n == 1:
        return 1
    while n > 1:
        temp.append(n % 3)
        n //= 3
        if n == 1:
            temp.append(n)
    for i in range(len(temp)):
        answer += int(temp[i]) * (3 ** (len(temp) - i - 1))
    return answer


print(solution(n))
