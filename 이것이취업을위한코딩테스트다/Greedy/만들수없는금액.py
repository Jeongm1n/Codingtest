from itertools import combinations
n = int(input())
data = list(map(int, input().split()))
temp = []
for i in range(1, n+1):
    temp.append(list(map(sum, combinations(data, i))))
answer = set([x for row in temp for x in row])
i = 1
result = -1
for n in answer:
    if n != i:
        result = i
        break
    i += 1
if result == -1:
    print(i)
else:
    print(result)