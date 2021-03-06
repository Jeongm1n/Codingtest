n = int(input())
people = list(map(int, input().split()))
index = []
count = 0
for i in range(n):
    if people[i] in index:
        count += 1
    else:
        index.append(people[i])
print(count)