def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer:
            answer[i[1]] += 1
        else:
            answer[i[1]] = 1
    cnt = 1
    for i in answer.value():
        cnt *= (i+1)
    return cnt-1
clothes = [list(map(str, input().split())) for _ in range(int(input()))]
print(solution(clothes))