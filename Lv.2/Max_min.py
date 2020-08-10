def solution(s):
    answer = []
    result=[]
    x=''
    answer=s.split(' ')
    for i in range(len(answer)):
        result.append(int(answer[i]))
    _max=str(max(result))
    _min=str(min(result))
    x=_min+' '+_max
    return x
    
print(solution("1 2 3 4"))