def solution(seoul):
    answer = ''
    index = 0
    for i in range(len(seoul)):
        if len(seoul[i])==3:
            if seoul[i][0]=='K' and seoul[i][1]=='i' and seoul[i][2]=='m':
                index=i
    answer="김서방은 "+str(index)+"에 있다"      
    return answer

a=["Jane", "Kim"]
print(solution(a))