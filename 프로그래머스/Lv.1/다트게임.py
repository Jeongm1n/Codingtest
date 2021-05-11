def solution(dartResult):
    score = {} 
    count = 0
    for i in range(len(dartResult)):
        if (dartResult[i] >= '0' and dartResult[i] <= '9'):
            if(dartResult[i] == '1' and dartResult[i+1] == '0'):
                score[count] = 10
                count+=1
            elif dartResult[i] == '0':
                if i == 0:
                    score[count] = 0
                    count += 1
                else:
                    if dartResult[i-1] == '1':
                        continue
                    else:
                        score[count] =  0
                        count += 1
            else:
                score[count] = int(dartResult[i])
                count+=1
        elif dartResult[i] == 'D':
            score[count-1] = score[count-1]**2
        elif dartResult[i] == 'T':
            score[count-1] = score[count-1]**3
        elif dartResult[i] == '*':
            if count == 1:
                score[count-1] = score[count-1]*2
            else:
                score[count-1] = score[count-1]*2
                score[count-2] = score[count-2]*2
        elif dartResult[i] == '#':
            score[count-1] = -score[count-1]
    return sum(score.values())

dartResult = input()
print(solution(dartResult))