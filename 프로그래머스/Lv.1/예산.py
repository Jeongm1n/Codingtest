def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
d = list(map(int, input().split()))
budget = int(input())
print(solution(d, budget))