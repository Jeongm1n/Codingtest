tempX = []
tempY = []
for _ in range(3):
    x, y = map(int, input().split())
    tempX.append(x)
    tempY.append(y)
for i in range(3):
    if tempX.count(tempX[i]) == 1:
        x = tempX[i]
    if tempY.count(tempY[i]) == 1:
        y = tempY[i]
print(x, y)