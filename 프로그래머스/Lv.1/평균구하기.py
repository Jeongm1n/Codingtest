def solution(arr):
    return sum(arr)/len(arr)
arr = list(map(int, input().split()))
print(solution(arr))