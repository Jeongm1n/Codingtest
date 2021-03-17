import sys
n = int(sys.stdin.readline())
data = [0] * 10001
for _ in range(n):
    num = int(sys.stdin.readline())
    data[num] += 1

for i in range(10001):
    if i != 0:
        for j in range(data[i]):
            print(i)