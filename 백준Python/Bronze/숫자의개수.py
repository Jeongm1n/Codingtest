a = int(input())
b = int(input())
c = int(input())
result = str(a*b*c)
for i in range(10):
    count = 0
    for j in range(len(result)):
        if result[j] == str(i):
            count += 1
    print(count)