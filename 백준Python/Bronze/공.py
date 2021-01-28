m = int(input())
answer = 1
for _ in range(m):
    x, y = map(int, input().split())
    if  x == answer or y == answer:
        if x == answer:
            answer = y
        elif y == answer:
            answer = x
print(answer)