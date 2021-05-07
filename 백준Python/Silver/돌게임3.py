n = int(input())
d = [0] * 1001
d[1], d[2], d[3], d[4] = 1, 0, 1, 1
for i in range(5, n + 1):
    if d[i - 4] + d[i - 3] + d[i - 1] != 3:
        d[i] = 1
if d[n] == 1:
    print("SK")
else:
    print("CY")
