def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer = answer + (a[i]*b[i])
    return answer
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solution(a, b))