t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input().split())
    answer = s[0]
    for i in range(1, n):
        if s[i] <= answer:
            answer = s[i] + answer
        else:
            answer += s[i]
    print(''.join(answer))