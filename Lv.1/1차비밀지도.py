def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = bin(arr1[i]|arr2[i])[2:]
        b = '0'*(n-len(a)) + a
        b = b.replace('1', '#')
        b = b.replace('0', ' ')
        answer.append(b)
    return answer

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(solution(n, arr1, arr2))