import sys

input = sys.stdin.readline
left = int(input())
right = int(input())


def divisor(num):
    cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cnt += 1
    if cnt % 2 == 0:
        return True
    else:
        return False


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if divisor(i):
            answer += i
        else:
            answer -= i
    return answer


print(solution(left, right))
