def solution(board):
    height = len(board)
    width = len(board[0])
    for i in range(1, height):
        for j in range(1, width):
            if board[i][j] >= 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
    return max([num for row in board for num in row])**2

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))
