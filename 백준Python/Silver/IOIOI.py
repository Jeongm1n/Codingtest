import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline()
answer, pattern, i = 0, 0, 1
while i < m - 1:
    if s[i - 1] == "I" and s[i] == "O" and s[i + 1] == "I":
        pattern += 1
        if pattern == n:
            answer += 1
            pattern -= 1
        i += 1
    else:
        pattern = 0
    i += 1
print(answer)
