s = input()
answer = [0]*26
for element in s:
    answer[ord(element)-97] = s.count(element)
print(*answer)