import sys
from itertools import combinations

input = sys.stdin.readline
nums = list(map(int, input().split()))


def solution(nums):
    n = len(nums) // 2
    nums = list(set(nums))
    if len(nums) > n:
        return n
    else:
        return len(nums)


print(solution(nums))
