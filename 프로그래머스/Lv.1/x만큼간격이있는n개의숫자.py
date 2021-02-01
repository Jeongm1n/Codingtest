def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
    return answer
x, n = map(int, input().split())
print(solution(x, n))