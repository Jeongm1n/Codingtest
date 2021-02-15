a, b, c = map(int, input().split())
d = int(input()) 

c += d % 60
d = d // 60
if c >= 60:
    c -= 60
    b += 1

b += d % 60
d = d // 60
if b >= 60:
    b -= 60
    a += 1

a += d % 24
if a >= 24:
    a -= 24

print(a,b,c)