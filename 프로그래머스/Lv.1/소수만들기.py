import sys
from itertools import combinations

input = sys.stdin.readline
nums = list(map(int, input().split()))


def isPrime(data):
    if sum(data) == 0 or sum(data) == 1:
        return False
    for i in range(2, (sum(data) // 2) + 1):
        if sum(data) % i == 0:
            return False
    return True


def solution(nums):
    nums = list(combinations(nums, 3))
    answer = 0
    for i in nums:
        if isPrime(i):
            answer += 1
    return answer


print(solution(nums))
