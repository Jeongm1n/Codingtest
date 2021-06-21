for _ in range(int(input())):
    n = int(input())
    d = [0] * 101
    d[1], d[2], d[3], d[4] = 1, 1, 1, 2
    for i in range(5, n + 1):
        d[i] = d[i - 2] + d[i - 3]
    print(d[n])
