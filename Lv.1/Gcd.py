import math
def solution(n, m):        
    return [math.gcd(n,m),int(n*m/math.gcd(n,m))]

a=3
b=12
print(solution(a,b))