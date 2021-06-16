import sys

input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
temp = sorted(list(set(data)))

dic = {temp[i]: i for i in range(len(temp))}
for i in data:
    print(dic[i], end=" ")
