a, b = map(int, input().split())
c = int(input())
a = a + (c//60)
b = b + (c%60)
if a >= 24:
    a = a - 24
if b >= 60:
    a = a + (b//60)
    if a >= 24:
        a = a - 24
    b = b%60
    
print(a, end=' ')
print(b)