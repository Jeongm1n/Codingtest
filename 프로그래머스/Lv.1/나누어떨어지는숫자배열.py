def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i]%divisor == 0:
            answer.append(arr[i])
    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer) if len(answer)!=0 else answer

arr = list(map(int, input().split()))
divisor = int(input())
print(solution(arr, divisor))