n = int(input())
data = [list(input().split()) for _ in range(n)]

data.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for s in data:
    print(s[0])
