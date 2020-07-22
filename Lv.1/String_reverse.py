def solution(s):
    answer = ''
    answer = ''.join(sorted(s, reverse=True))
    return answer

a="Zbcdefg"
print(solution(a))