def solution(s):
    return ''.join(sorted(s, reverse=True))
s = input()
print(solution(s))