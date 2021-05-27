def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    cnt = 0
    temp, i, j, k = 0, 0, 0, 0
    while cnt < len(arr1)*len(arr2[0]): 
        if i == len(arr1):
            i = 0
            k += 1
            continue
        while j < len(arr1[0]):
            temp += (arr1[i][j] * arr2[j][k])
            j += 1
        answer[i][k] = temp
        i += 1
        cnt += 1
        j = 0
        temp = 0
    return answer
arr1 = [list(map(int, input().split())) for _ in range(int(input()))]
arr2 = [list(map(int, input().split())) for _ in range(int(input()))]
print(solution(arr1, arr2))