n = int(input())
n = str(n)
half = len(n)//2

front, rear = 0, 0
for i in range(half):
    front += int(n[i])
for i in range(half, len(n)):
    rear += int(n[i])
if front == rear:
    print('LUCKY')
else:
    print('READY')