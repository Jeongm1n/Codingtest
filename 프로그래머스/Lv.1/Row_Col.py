def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j]+=arr2[i][j]
    return arr1
a=[[1,2],[2,3]]
b=[[3,4],[5,6]]
print(solution(a,b))