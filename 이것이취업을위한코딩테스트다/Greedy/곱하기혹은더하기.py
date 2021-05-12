s = input()
s = list(map(int, s))
answer = s[0]
for i in range(1, len(s)):
    if answer <= 1 or s[i] <= 1:
        answer += s[i]
    else:
        answer *= s[i]
print(answer)