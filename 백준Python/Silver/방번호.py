import math

temp = [0] * 11
n = int(input())
n = str(n)
for i in range(len(n)):
    if int(n[i]) == 6 or int(n[i]) == 9:
        temp[10] += 1
    else:
        temp[int(n[i])] += 1
if temp.index(max(temp)) == 10:
    print(math.ceil(max(temp) / 2))
else:
    print(max(temp))
