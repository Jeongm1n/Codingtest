from collections import deque
n = int(input())
q = deque()
answer = []
for _ in range(n):
    s = input()
    if 'push_back' in s:
        q.append(int(s.split(' ')[1]))
    if 'push_front' in s:
        q.appendleft(int(s.split(' ')[1]))
    if s == 'front':
        if len(q) > 0:
            answer.append(q[0])
        else:
            answer.append(-1)
    if s == 'back':
        if len(q) > 0:
            answer.append(q[len(q)-1])
        else:
            answer.append(-1)
    if s == 'size':
        answer.append(len(q))
    if s == 'empty':
        if len(q) > 0:
            answer.append(0)
        else:
            answer.append(1)
    if s == 'pop_front':
        if len(q) > 0:
            answer.append(q.popleft())
        else:
            answer.append(-1)
    if s == 'pop_back':
        if len(q) > 0:
            answer.append(q.pop())
        else:
            answer.append(-1)
for ans in answer:
    print(ans)