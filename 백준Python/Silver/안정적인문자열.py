answer = []
while True:
    s = input()
    stack = []
    count = 0
    if "-" in s:
        break
    for i in range(len(s)):
        if not stack and s[i] == "}":
            count += 1
            stack.append("{")
        elif stack and s[i] == "}":
            stack.pop()
        else:
            stack.append("{")
    count += len(stack) // 2
    answer.append(count)
for i in range(1, len(answer) + 1):
    print(i, ". ", answer[i - 1], sep="")
