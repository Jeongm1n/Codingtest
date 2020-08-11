def solution(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    answer=x%1234567
    return answer
print(solution(5))