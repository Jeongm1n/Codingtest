n = int(input())
x, y = map(int, input().split())
answer = 0
for i in range(n-1):
    temp_x, temp_y = map(int, input().split())
    if temp_x == x:
        y = temp_y
    elif y >= temp_x and temp_y > y:
        y = temp_y
    elif y < temp_x:
        answer += abs(x-y)
        x = temp_x
        y = temp_y
print(answer + abs(y-x))