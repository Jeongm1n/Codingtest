n = int(input())
b = list(map(int, input().split()))
answer = 0
while sum(b) > 0:
    if 1 in b:
        b[b.index(1)] -= 1
        answer += 1
    else:
        for i in range(len(b)):
            if b[i]%2 == 1:
                b[i] -= 1
                answer += 1
        for i in range(len(b)):
            b[i] //= 2
        answer += 1
print(answer)