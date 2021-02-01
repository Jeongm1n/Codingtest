def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                answer = True
            else:
                answer = False
                break
    return answer
s = input()
print(solution(s))