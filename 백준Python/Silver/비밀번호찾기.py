import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dic = {}
for _ in range(n):
    data = input().split()
    dic[data[0]] = data[1]
for _ in range(m):
    site = input().rstrip()
    print(dic[site])
