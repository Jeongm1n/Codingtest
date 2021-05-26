def z(n, x, y):
    global answer
    if x == r and y == c:
        print(int(answer))
        exit(0)
    if n == 1:
        answer += 1
        return
    if not (x <= r < x + n and y <= c < y + n):
        answer += n ** 2
        return
    z(n / 2, x, y)
    z(n / 2, x, y + n / 2)
    z(n / 2, x + n / 2, y)
    z(n / 2, x + n / 2, y + n / 2)


n, r, c = map(int, input().split())
answer = 0
z(2 ** n, 0, 0)
