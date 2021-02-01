def solution(arr):
    num = str(arr)
    sum_value = 0
    for i in range(len(num)):
        sum_value += int(num[i])
    return True if arr%sum_value == 0 else False
arr = int(input())
print(solution(arr))