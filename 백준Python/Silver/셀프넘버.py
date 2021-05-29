nums = set(range(1, 10001))
temp = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    temp.add(i)

selfnums = sorted(nums - temp)
for selfnum in selfnums:
    print(selfnum)
