import sys
answer = []
for i in range(3):
    s = sum([int(sys.stdin.readline()) for j in range(int(sys.stdin.readline()))])
    answer.append('0' if s==0 else '-' if s<0 else '+' )
print('\n'.join(answer))