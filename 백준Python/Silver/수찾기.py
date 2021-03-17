import sys
n = int(sys.stdin.readline())
a = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
for num in b:
    sys.stdout.write('1\n') if num in a else sys.stdout.write('0\n')