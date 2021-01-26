numbers = list(map(int, input().split()))
answer = 0
for i in range(5):
    answer += (numbers[i]**2)
print(answer%10)