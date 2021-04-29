wUniv = []
kUniv = []
for i in range(20):
    if i < 10:
        wUniv.append(int(input()))
    else:
        kUniv.append(int(input()))
wUniv.sort(reverse=True)
kUniv.sort(reverse=True)
print(sum(wUniv[:3]), sum(kUniv[:3]))