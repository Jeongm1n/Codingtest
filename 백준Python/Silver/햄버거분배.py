n, k = map(int, input().split())
s = input()
s = list(s)
cnt = 0
for i in range(len(s)):
    if s[i] == "P":
        for j in range(i - k, i + k + 1):
            if 0 <= j < n and s[j] == "H":
                cnt += 1
                s[j] = "-"
                break
print(cnt)
