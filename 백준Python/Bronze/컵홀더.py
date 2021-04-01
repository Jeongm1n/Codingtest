n = int(input())
sit = input()
cnt, i = 0, 0
while i < len(sit):
    cnt += 1
    if sit[i] == 'L':
        i += 2
    else:
        i += 1
if 'L' in sit:
    print(cnt+1)
else:
    print(cnt)