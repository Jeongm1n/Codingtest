n = int(input())
check = n
new_n = 0
temp = 0
count = 0
while 1:
    temp = n//10 + n%10
    new_n = (n%10)*10 + temp%10
    count += 1
    n = new_n
    if new_n == check:
        break
print(count)