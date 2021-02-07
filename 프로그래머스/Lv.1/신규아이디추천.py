def solution(new_id):
# 1단계 ~ 2단계
    char = []
    for i in range(26):
        char.append(chr(i+97))
        if i < 10:
            char.append(chr(i+48))
    char += '-_.'
    new_id = new_id.lower()
    temp1 = ''
    for element in new_id:
        if element in char:
            temp1 += element
# 3단계 ~ 5단계
    temp2 = temp1[0]
    for i in range(1, len(temp1)):
        if temp1[i] == '.' and temp1[i] == temp1[i-1]:
            continue
        temp2 += temp1[i]
    temp3 = list(temp2)
    if temp3[0] == '.':
        del temp3[0]
        if len(temp3) == 0:
            temp3.append('a')
    if temp3[len(temp3)-1] == '.':
        del temp3[len(temp3)-1]
    temp4 = ''.join(temp3)
# 6단계    
    if len(temp4) > 15:
        temp5 = temp4[:15]
        if temp5[len(temp5)-1] == '.':
            temp5 = temp4[:14]
    else: 
        temp5 = temp4
# 7단계
    idx = temp5[len(temp5)-1]
    if len(temp5) <= 2:
        while len(temp5) < 3:
            temp5 += idx
    return temp5
new_id = input()
print(solution(new_id))