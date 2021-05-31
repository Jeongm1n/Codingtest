n = int(input())
array = [int(input()) for _ in range(n)]
array.sort(reverse=True)
answer = 0
for i in range(n):
    if array[i] - ((i + 1) - 1) > 0:
        answer += array[i] - ((i + 1) - 1)
print(answer)
