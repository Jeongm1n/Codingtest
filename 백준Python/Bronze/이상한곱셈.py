n = input().split()
a = list(map(int, n[0]))
b = list(map(int, n[1]))
b = sum(b)
answer = 0
for i in range(len(a)):
    answer += a[i]*(b)
print(answer)