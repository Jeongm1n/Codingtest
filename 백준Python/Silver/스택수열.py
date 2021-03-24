n = int(input())
count = 1
stack = []
answer = []
message = True
for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        answer.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        message = False
if message == False:
    print('NO')
else:
    for n in answer:
        print(n)