def solution(v):
    idx1=0
    idx2=0
    if v[0][0] == v[1][0]:
        idx1 = v[2][0]
    elif v[0][0] == v[2][0]:
        idx1 = v[1][0]
    elif v[2][0] == v[1][0]:
        idx1 = v[0][0]
    
    if v[0][1] == v[1][1]:
        idx2 = v[2][1]
    elif v[0][1] == v[2][1]:
        idx2 = v[1][1]
    elif v[2][1] == v[1][1]:
        idx2 = v[0][1]
        
    return [idx1, idx2]

print(solution([[1, 4], [3, 4], [3, 10]]))