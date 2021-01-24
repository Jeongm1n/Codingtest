def solution(n):
    answer = []
    _list=str(n)
    for i in range(len(_list)-1, -1, -1):
        answer.append(int(_list[i]))
    return answer
a=12345
print(solution(a))