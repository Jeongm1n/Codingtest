def solution(s):
    answer = ''
    index = len(s)//2
    if len(s) % 2 == 0:
        answer = s[index-1]+s[index]
    else:
        answer = s[index]
    return answer
s = input()
print(solution(s))