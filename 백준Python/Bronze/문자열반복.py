t = int(input())
for _ in range(t):
    r, s = input().split()
    answer = ''
    for element in s:
        answer += element*int(r)
    print(answer)