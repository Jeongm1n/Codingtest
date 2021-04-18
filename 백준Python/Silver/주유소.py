n = int(input())
distance = list(map(int, input().split()))
oil = list(map(int, input().split()))
answer = 0
start = oil[0]
for i in range(n-1):
    if oil[i] < start:
        start = oil[i]
    answer += (start*distance[i])
print(answer)