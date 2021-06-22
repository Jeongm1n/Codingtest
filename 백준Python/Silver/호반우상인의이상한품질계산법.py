n = int(input())
data = list(map(int, input().split()))
data.sort()
answer = 0
if n%2 == 0:
    for i in range(len(data)-1, len(data)//2-1, -1):
        answer += (data[i]*2)
else:
    for i in range(len(data)-1, len(data)//2-1, -1):
        if i > len(data)//2:
            answer += (data[i]*2)
        else:
            answer += data[i]
print(answer)