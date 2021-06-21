change = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
s = input()
temp = [s[0]]
answer = 1
for i in range(1, len(s)):
    temp.append(s[i])
    answer += 1
    if s[i - 2] + s[i - 1] + s[i] == "dz=":
        answer -= 1
    if s[i - 1] + s[i] in change:
        answer -= 1
print(answer)
