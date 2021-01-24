def solution(answers):
    result=[]
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []
    for i in range(len(answers)):
        if answers[i] == a[i%len(a)]:
            score[0] += 1
        if answers[i] == b[i%len(b)]:
            score[1] += 1
        if answers[i] == c[i%len(c)]:
            score[2] += 1
    Max=max(score)
    result.append(score.index(max(score))+1)
    for i in range(3):
        if i==score.index(max(score)):
            continue
        if Max==score[i]:
            result.append(i+1)
    return result
        

answer=[1,3,2,4,2]
print(solution(answer))