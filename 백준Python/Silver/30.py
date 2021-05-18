n = list(input())
n.sort(reverse=True)
sumValue = 0
for i in n:
    sumValue += int(i)
if sumValue % 3 != 0 or "0" not in n:
    print(-1)
else:
    print("".join(n))
