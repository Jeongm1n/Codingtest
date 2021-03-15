n = int(input())
l = list(map(int, input().split()))
answer = 0
while len(l) > 1:
    if l.index(max(l)) == len(l)-1:
        answer += (max(l) + l[len(l)-2])
        l.pop(len(l)-2)
    elif l.index(max(l)) == 0:
        answer += (max(l) + l[1])
        l.pop(1)
    else:
        answer += (max(l) + l[l.index(max(l))-1])
        l.pop(l.index(max(l))-1)
print(answer)