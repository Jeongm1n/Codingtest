from itertools import permutations

def solution(numbers):
    a=set()
    for i in range(len(numbers)):
        a|=set(map(int, map("".join, permutations(list(numbers), i+1))))
        # 모든 경우의 수를 만듬 
    a-=set(range(0,2))
    # 숫자 0과 1은 제거 
    
    # 모든 경우의 수에 대해서 소수 판정
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

"""  ==>> 시간초과 문제
    answer=0
    for key in a:
        cnt=0
        for j in range(1, key+1):
            if key%j==0:
                cnt+=1
        if cnt==2:
            answer+=1
    return answer
"""

numbers="011"
print(solution(numbers))