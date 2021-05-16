answer = 0
for _ in range(int(input())):
    word = input()
    alpha = [0] * 26
    flag, i = True, 1
    alpha[ord(word[0]) - 97] = 1
    tempIdx = ord(word[0]) - 97
    while i < len(word):
        if ord(word[i]) - 97 == tempIdx or alpha[ord(word[i]) - 97] == 0:
            alpha[ord(word[i]) - 97] += 1
            tempIdx = ord(word[i]) - 97
            i += 1
        else:
            flag = False
            break
    if flag == True:
        answer += 1
print(answer)
