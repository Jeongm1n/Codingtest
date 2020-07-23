def solution(strings, n):
    return sorted(sorted(strings), key= lambda x : x[n])

a = ["abce", "abcd", "cdx"]
n = int(input())
print(solution(a, n))