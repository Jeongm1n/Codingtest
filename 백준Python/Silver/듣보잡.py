import sys
n, m = map(int, sys.stdin.readline().split())
a = [sys.stdin.readline().strip() for i in range(n)]
b = [sys.stdin.readline().strip() for i in range(m)]
answer = list(set(a) & set(b))
print(len(answer))
for n in sorted(answer):
    print(n)