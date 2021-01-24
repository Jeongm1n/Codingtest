def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i]%divisor==0:
            answer.append(arr[i])
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer

a=[5,7,9,10]
n=5
print(solution(a,n))