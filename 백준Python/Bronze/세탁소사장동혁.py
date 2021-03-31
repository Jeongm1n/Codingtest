t = int(input())
for _ in range(t):
    c = int(input())
    exchange = [0] * 4
    exchange[0] = c//25
    c %= 25
    exchange[1] = c//10
    c %= 10
    exchange[2] = c//5
    c %= 5
    exchange[3] = c//1
    print(*exchange)