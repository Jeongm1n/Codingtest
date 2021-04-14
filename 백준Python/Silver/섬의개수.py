while 1:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    board = []
    for _ in range(m):
        board.append(list(map(int, input().split())))

    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    def bfs(x, y):
        queue = []
        queue.append([x, y])
        while queue:
            x, y = queue.pop(0)
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if board[nx][ny] == 0:
                    continue
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    queue.append([nx, ny])

    answer = 0
    for i in range(m):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                board[i][j] = 0
                bfs(i, j)
                answer += 1
    print(answer)