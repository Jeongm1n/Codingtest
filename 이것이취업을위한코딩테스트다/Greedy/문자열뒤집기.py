s = input()
temp = s[0]
temp_s = []
for i in range(1, len(s)):
    if s[i] != temp:
        temp_s.append(s[i-1])
        temp = s[i]
    if i == len(s)-1:
        temp_s.append(temp)
print(min(temp_s.count('0'), temp_s.count('1')))