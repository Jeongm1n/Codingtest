def solution(s):
    ########Stack########
    stack = []
    for x in s:
        if x=='(':
            stack.append(x)
        else:
            if len(stack)==0:
                return False
            else:
                stack.pop()
    return len(stack)==0 #if
        
    

a="()()("
print(solution(a))