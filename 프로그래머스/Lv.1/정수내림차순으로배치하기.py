def solution(n):
    number = list(str(n))
    number.sort(reverse=True)
    return int(''.join(number))
n = int(input())
print(solution(n))