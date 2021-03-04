chess = [1, 1, 2, 2, 2, 8]
current = list(map(int, input().split()))
for i in range(len(chess)):
    if chess[i] == current[i]:
        print(int('0'), end=' ')
    else:
        print(chess[i]-current[i], end=' ')