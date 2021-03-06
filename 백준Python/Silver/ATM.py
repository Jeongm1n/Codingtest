n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0
temp = 0
for i in range(n):
    temp += arr[i]
    answer += temp
print(answer)