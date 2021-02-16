def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] != 0:
                board[i][j] = min(board[i][j-1], board[i-1][j], board[i-1][j-1]) + 1
    return max([element for row in board for element in row])**2
board = [list(map(int, input().split())) for _ in range(int(input()))]
print(solution(board))