s = input()
answer = []
digit = 0
for element in s:
    if element.isalpha():
        answer.append(element)
    else:
        digit += int(element)
answer.sort()
print(''.join(answer)+str(digit))