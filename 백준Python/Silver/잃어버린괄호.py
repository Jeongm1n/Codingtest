s = input().split('-')
temp = []
for i in s:
    cnt = 0
    plus = i.split('+')
    for j in plus:
        cnt += int(j)
    temp.append(cnt)
first = temp[0]
for i in range(1, len(temp)):
    first -= temp[i]
print(first)