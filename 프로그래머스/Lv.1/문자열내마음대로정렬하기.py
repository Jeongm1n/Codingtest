def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n]) 
strings = list(input().split())
n = int(input())
print(solution(strings, n))