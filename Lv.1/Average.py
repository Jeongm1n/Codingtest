def solution(arr):
    answer = 0
    for i in range(len(arr)):
        answer+=arr[i]
        
    return answer/len(arr)

a=[1,2,3,4]
print(solution(a))