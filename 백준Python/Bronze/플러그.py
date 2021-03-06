import sys
n = int(sys.stdin.readline())
array = []
for _ in range(n):
    a = int(sys.stdin.readline())
    array.append(a)

answer = 0
for i in range(n):
    if i == n-1:
        answer += array[i]
    else:
        answer += array[i]-1
    
print(answer)