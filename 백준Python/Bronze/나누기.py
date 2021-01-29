n = int(input())
f = int(input())

n //= 100
n *= 100

while n % f != 0:
    n += 1
n %= 100
if n < 10:
    print("0%d"%n)
else:
    print(n)