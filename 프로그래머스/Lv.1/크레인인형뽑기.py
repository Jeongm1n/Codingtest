def solution(board, moves):
    basket = []
    answer = 0
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] == 0:
                continue
            basket.append(board[j][moves[i]-1])
            board[j][moves[i]-1] = 0
            if len(basket) != 1 and basket[len(basket)-1] == basket[len(basket)-2]:
                del basket[len(basket)-1]
                del basket[len(basket)-1]
                answer += 2
            break
    return answer
n = int(input())
board = [list(map(int, input().split())) for i in range(n)]
moves = list(map(int, input().split()))
print(solution(board, moves))