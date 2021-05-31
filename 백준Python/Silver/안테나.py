n = int(input())
data = list(map(int, input().split()))
data.sort()
dist = 0
if len(data) % 2 == 1:
    print(data[len(data) // 2])
else:
    mid1, mid2 = data[len(data) // 2], data[(len(data) // 2) - 1]
    temp1, temp2 = 0, 0
    for i in data:
        temp1 += abs(mid1 - i)
        temp2 += abs(mid2 - i)
    if temp1 < temp2:
        print(data[len(data) // 2])
    else:
        print(data[len(data) // 2 - 1])
