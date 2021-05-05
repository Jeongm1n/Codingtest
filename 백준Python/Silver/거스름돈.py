# n = int(input())
# if n in [1, 3]:
#     answer = -1
# elif (n%5)%2 == 0:
#     answer = n//5 + (n%5)//2
# else:
#     answer = ((n//5)-1) + ((n%5+5)//2)
# print(answer)
n = int(input())
d = [-1] * 100001
d[0], d[2], d[5] = 0, 1, 1
for i in range(1, n + 1):
    if i >= 2 and d[i - 2] > -1:
        d[i] = d[i - 2] + 1
    if i >= 5 and d[i - 5] > -1:
        d[i] = min(d[i], d[i - 5] + 1)
print(d[n])
