n = int(input())
d = [5001]*5001
d[0] = 0
d[3], d[5] = 1, 1
for i in range(6, n+1):
    d[i] = min(d[i-3], d[i-5])+1
if d[n] > 5000:
    print(-1)
else:
    print(d[n])