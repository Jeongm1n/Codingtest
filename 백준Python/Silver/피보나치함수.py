t = int(input())
for _ in range(t):
    n = int(input())
    zero = 1
    one = 0
    temp = 0
    for _ in range(n):
        temp = zero
        zero = one
        one = temp + one
    print(zero, one)