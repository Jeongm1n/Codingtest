for _ in range(3):
    a, b, c, d = map(int, input().split())
    sumValue = a + b + c + d
    if sumValue == 3:
        print('A')
    elif sumValue == 2:
        print('B')
    elif sumValue == 1:
        print('C')
    elif sumValue == 4:
        print('E')
    else:
        print('D')