import math
def solution(n):
    answer = []
    result = 0
    while n>0:
        answer.append(n%3)
        n //= 3
    print(answer)
    i = len(answer)-1
    j = 0
    while 1:
        result += (answer[j]*math.pow(3, i))
        i -= 1
        j += 1
        if i == -1:
            break
    return result
    

print(solution(45))