def solution(s):
    answer = ''
    result=[]
    answer=s.split(' ')
    for i in range(len(answer)):
        result.append(answer[i].capitalize())
    return ' '.join(result)

print(solution("3people unFollowed me"))