t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0]*n for _ in range(m)]
    for _ in range(k):
        a, b = map(int, input().split())
        board[a][b] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = 0

    def bfs(x, y):
        queue = [[x, y]]
        while queue:
            x, y = queue.pop(0)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if board[nx][ny] == 0:
                    continue
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    queue.append([nx, ny])

    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                board[i][j] = 0
                bfs(i, j)
                answer += 1
    print(answer)