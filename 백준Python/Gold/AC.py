import sys


def AC(command, data, n):
    command.replace("RR", "")
    l, r, d = 0, 0, True
    for c in command:
        if c == "R":
            d = not d
        elif c == "D":
            if d:
                l += 1
            else:
                r += 1
    if l + r <= n:
        answer = data[l : n - r]
        if d:
            return "[" + ",".join(answer) + "]"
        else:
            return "[" + ",".join(answer[::-1]) + "]"
    else:
        return "error"


input = sys.stdin.readline
for _ in range(int(input())):
    command = input()
    n = int(input())
    data = input().rstrip()[1:-1].split(",")
    if n == 0:
        data = []
    print(AC(command, data, n))
