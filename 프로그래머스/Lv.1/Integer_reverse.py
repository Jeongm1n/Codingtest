def solution(n):
    answer = 0
    _list=list(str(n))
    _list.sort(reverse=True)
    answer = int("".join(_list))    
    return answer
a=118372
print(solution(a))