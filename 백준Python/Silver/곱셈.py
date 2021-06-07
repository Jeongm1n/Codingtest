import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())


def func(length):
    if length == 1:
        return a % c
    if length % 2 == 0:
        temp = func(length // 2)
        return temp * temp % c
    else:
        temp = func(length // 2)
        return temp * temp * a % c


print(func(b))
