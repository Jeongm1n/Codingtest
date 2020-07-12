from math import sqrt, pow
def solution(n):
    if sqrt(n)%1==0:
        return int(pow(sqrt(n)+1,2))
    else:
        return -1

a=122
print(solution(a))