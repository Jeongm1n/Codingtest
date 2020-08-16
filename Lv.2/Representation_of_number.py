def solution(n):
    cnt=0
    for i in range(1, n+1):
        answer=0
        for j in range(i,n+1):
            answer+=j
            if answer==n:
                cnt+=1
                break
            elif answer>n:
                break
    return cnt

print(solution(15))