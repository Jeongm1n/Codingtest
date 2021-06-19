import sys

input = sys.stdin.readline

a, b = map(int, input().split())

temp = []
for i in range(1, 46):
    temp += [i] * i

print(sum(temp[a - 1 : b]))
