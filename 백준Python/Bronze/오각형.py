n = int(input())
answer = 0
for i in range(1, n+1):
    answer += (3*i + 1) % 45678
print((answer+1)%45678)