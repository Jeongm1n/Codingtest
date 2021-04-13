r, c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(input()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

flag = True
for i in range(r):
    if flag == False:
        break
    for j in range(c):
        if graph[i][j] == 'W':
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or ny < 0 or nx >=r or ny >= c:
                    continue
                if graph[nx][ny] == 'S':
                    flag = False
                    break
        elif graph[i][j] == 'S':
            continue
        elif graph[i][j] == '.':
            graph[i][j] = 'D'

if flag == False:
    print(0)
else:
    print(1)
    for i in graph:
        print(''.join(i))