import sys
from itertools import product

input = sys.stdin.readline

target = int(input())
numbers = list(map(int, input().split()))


def solution(numbers, target):
    i = [(x, -x) for x in numbers]
    j = list(map(sum, product(*i)))
    return j.count(target)


print(solution(numbers, target))
