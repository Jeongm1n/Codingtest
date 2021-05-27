import math
def solution(arr):
    answer = arr[0]
    for n in arr:
        answer = n*answer//math.gcd(n, answer)
    return answer
arr = list(map(int, input().split()))
print(solution(arr))