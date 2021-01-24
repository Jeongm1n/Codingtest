def solution(n):
    index1=n
    index2=n
    cnt=0
    while n>=1:
        if n%2==1:
            cnt+=1
            n=int(n/2)
        else:
            n=int(n/2)

    answer=0
    while 1:
        index1+=1
        index2=index1
        count=0
        while index2>=1:
            if index2%2==1:
                count+=1
                index2=int(index2/2)
            else:
                index2=int(index2/2)
        if cnt==count:
            answer=index1
            break
        else:
            continue
    return answer