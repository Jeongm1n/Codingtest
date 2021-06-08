s = input()
data = []
for i in range(len(s)):
    data.append(s[i:])
data.sort()
for element in data:
    print(element)
