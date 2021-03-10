while 1:
    s = input()
    if s == '.':
        break
    stack = []
    answer = True
    for element in s:
        if element == '(' or element == '[':
            stack.append(element)
        if element == ')' and len(stack) > 0:
            if stack[len(stack)-1] == '(':
                stack.pop()
            else:
                answer = False
                break
        elif element == ')' and len(stack) == 0:
            answer = False
            break
        if element == ']' and len(stack) > 0:
            if stack[len(stack)-1] == '[':
                stack.pop()
            else:
                answer = False
                break
        elif element == ']' and len(stack) == 0:
            answer = False
            break
    if len(stack) > 0 or answer == False:
        print('no')
    elif answer == True:
        print('yes')