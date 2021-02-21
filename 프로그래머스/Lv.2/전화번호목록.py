def solution(phone_book):
    phone_book.sort()
    for a, b in zip(phone_book, phone_book[1:]):
        if a in b:
            return False
    return True
phone_book = list(map(str, input().split()))
print(solution(phone_book))
