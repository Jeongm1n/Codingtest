def solution(s):
    stack = []
    for element in s:
        if element == '(':
            stack.append(element)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0
print(solution(input()))