def solution(n):
    if n <= 3:
        return '124'[n-1]
    else:
        x, y = divmod(n-1, 3)
        return solution(x) + '124'[y]
    
print(solution(int(input())))