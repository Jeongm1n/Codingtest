n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()
max_value = data[0]*len(data)
for i in range(1, len(data)):
    if data[i]*(len(data)-i) > max_value:
        max_value = data[i]*(len(data)-i)
print(max_value)