n = int(input())
file = list(map(int, input().split()))
cluster = int(input())

count = 0
for i in range(n):
    if file[i] == 0:
        continue
    elif file[i] <= cluster:
        count += 1
    else:
        count += (file[i]//cluster)
        if file[i] % cluster > 0:
            count += 1
print(cluster*count)