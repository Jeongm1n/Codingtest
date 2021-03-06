import sys

input = sys.stdin.readline
n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp1 = bin(arr1[i] | arr2[i])[2:]
        temp2 = "0" * (n - len(temp1)) + temp1
        temp2 = temp2.replace("0", " ")
        temp2 = temp2.replace("1", "#")
        answer.append(temp2)
    return answer


print(solution(n, arr1, arr2))
