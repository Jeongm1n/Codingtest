import sys

input = sys.stdin.readline
phone_book = list(map(str, input().split()))


def solution(phone_book):
    phone_book.sort()
    for a, b in zip(phone_book, phone_book[1:]):
        if a == b[: len(a)]:
            return False
    return True


print(solution(phone_book))
