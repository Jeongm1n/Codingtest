n = int(input())
data = []
for _ in range(n):
    x, y = map(str, input().split())
    data.append((int(x), y))
data.sort(key=lambda x: x[0])
for element in data:
    print(element[0], element[1])