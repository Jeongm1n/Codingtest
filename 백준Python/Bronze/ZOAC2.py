s = input()
start = 'A'
answer = 0
for alphabet in s:
    left = ord(start) - ord(alphabet)
    right = ord(alphabet) - ord(start)
    if left < 0:
        left += 26
    if right < 0:
        right += 26
    answer += min(left, right)
    start = alphabet
print(answer)