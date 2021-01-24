def solution(board, moves):
    answer = 0
    box=[]
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1]!=0:
                box.append(board[j][moves[i]-1])
                board[j][moves[i]-1]=0
                break
    length=len(box)
    i=0    
    while i<length-1:
        if box[i]==box[i+1]:
            del box[i]
            del box[i]
            i = -1
            length=len(box)
            answer+=1
        i+=1
    return answer*2

board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
print(solution(board, moves))