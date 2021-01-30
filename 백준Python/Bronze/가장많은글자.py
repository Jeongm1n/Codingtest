l = [0]*26
while 1:
    try:
        n = input()
        if not(n):
            break
    except:
        exit()
    for c in n:
        if ord(c) != 10 and ord(c) != 32:
            l[ord(c) - 97] += 1
res=''
for i in range(26):
    res += chr(i+97) if l[i] == max(l) else ''

answer = sorted(res)
print(''.join(answer))