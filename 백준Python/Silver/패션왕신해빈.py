import sys


def func(clothes):
    dic = {}
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1
    cnt = 1
    for i in dic.values():
        cnt *= i + 1
    return cnt - 1


for _ in range(int(sys.stdin.readline())):
    clothes = [
        list(map(str, sys.stdin.readline().split()))
        for _ in range(int(sys.stdin.readline()))
    ]
    print(func(clothes))
