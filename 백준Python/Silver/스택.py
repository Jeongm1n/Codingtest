n = int(input())
stack = []
answer = []
for _ in range(n):
    s = input()
    if 'push' in s:
        num = int(s.split(' ')[1])
        stack.append(num)
    if s == 'top':
        if len(stack) > 0:
            answer.append(stack[len(stack)-1])
        else:
            answer.append(-1)
    if s == 'size':
        answer.append(len(stack))
    if s == 'empty':
        if len(stack) > 0:
            answer.append(0)
        else:
            answer.append(1)
    if s == 'pop':
        if len(stack) > 0:
            answer.append(stack.pop())
        else:
            answer.append(-1)
for ans in answer:
    print(ans)