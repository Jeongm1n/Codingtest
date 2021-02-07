def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1)):
            arr1[i][j] += arr2[i][j]
    return arr1
n = int(input())
arr1 = [list(map(int, input().split())) for i in range(n)]
arr2 = [list(map(int, input().split())) for i in range(n)]
print(solution(arr1, arr2))