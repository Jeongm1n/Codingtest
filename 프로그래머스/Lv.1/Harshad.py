def solution(x):
    return x % sum([int(str(x)[i]) for i in range (len(str(x)))]) == 0

arr=10
print(solution(arr))