for _ in range(int(input())):
    s = input()
    stack = []
    temp = True
    for element in s:
        if element == '(':
            stack.append('(')
        if element == ')' and len(stack) > 0:
            stack.pop()
        elif element == ')' and len(stack) == 0:
            temp = False
            break
    if temp == False or len(stack) > 0:
        print('NO')
    elif temp == True or len(stack) == 0:
        print('YES')