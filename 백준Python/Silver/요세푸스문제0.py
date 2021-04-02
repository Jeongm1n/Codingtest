from collections import deque
n, k = map(int, input().split())
data = deque([])
for i in range(1, n+1):
    data.append(i)
print('<', end='')
while data:
    for i in range(k-1):
        data.append(data[0])
        data.popleft()
    print(data.popleft(), end='')
    if data:
        print(', ', end='')
print('>')