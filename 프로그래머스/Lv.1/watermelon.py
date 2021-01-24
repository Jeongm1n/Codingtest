def solution(n):
    answer=''
    i = 0
    while i != n :
        if i%2==0:
            answer+='수'
        elif i%2==1:
            answer+='박'
        i+=1        
    return answer

num=int(input())
print(solution(num))