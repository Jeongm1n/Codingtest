def solution(n):
    return sum([int(x) for x in str(n)])
n = int(input())
print(solution(n))