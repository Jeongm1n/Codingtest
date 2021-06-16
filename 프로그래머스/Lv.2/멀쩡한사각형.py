import sys
import math

input = sys.stdin.readline

w, h = map(int, input().split())


def solution(w, h):
    return w * h - (w + h - math.gcd(w, h))


print(solution(w, h))
