import sys

input = sys.stdin.readline
numbers = list(map(int, input().split()))


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(numbers)))


print(solution(numbers))
