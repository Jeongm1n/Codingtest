def solution(progresses, speeds):
    answer = []
    result=[]
    i=0
    cnt=0
    while progresses[i]<100 and i<len(progresses):
        progresses[i]+=speeds[i]
        cnt+=1
        if progresses[i]>=100:
            result.append(cnt)
            cnt=0
            i+=1
            if i==len(progresses):
                break
    i=0
    while 1:
        cnt=0
        for j in range(i, len(result)):
            if result[i]>=result[j]:
                cnt+=1
            else:
                i=j
                break
        answer.append(cnt)
        if sum(answer)==len(result):
            break
    return answer

progresses=[10,20,30,40]
speeds=[40, 60, 10, 20]
print(solution(progresses, speeds))