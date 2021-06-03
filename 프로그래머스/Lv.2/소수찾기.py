import sys
from itertools import permutations

input = sys.stdin.readline

numbers = input().rstrip()


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        temp = list(((map(int, map("".join, permutations(numbers, i + 1))))))
        print(temp)
        for n in temp:
            if isPrime(n):
                answer.append(n)
    return len(set(answer))


print(solution(numbers))
