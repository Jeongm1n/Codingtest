import math
cross, height, width = map(int, input().split())
temp = math.sqrt((cross**2) / (height**2 + width**2))
print(int(temp*height), end=' ')
print(int(temp*width))