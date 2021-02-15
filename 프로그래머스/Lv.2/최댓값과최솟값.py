def solution(s):
    s = list(map(int, s.split(' ')))
    answer = map(str, [min(s), max(s)])
    return ' '.join(answer)
print(solution(input()))