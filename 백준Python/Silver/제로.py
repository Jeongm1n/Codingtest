k = int(input())
answer = []
for _ in range(k):
    num = int(input())
    if num == 0:
        answer.pop()
        continue
    answer.append(num)
print(sum(answer))