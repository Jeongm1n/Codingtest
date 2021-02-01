import math
def solution(n, m):        
    return [math.gcd(n,m),int(n*m/math.gcd(n,m))]
n, m = map(int, input().split())
print(solution(n, m))