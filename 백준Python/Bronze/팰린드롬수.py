while 1:
    num = input()
    if num == '0':
        break
    answer = ''
    for i in range(len(num)//2):
        if num[(len(num)-1)-i] == num[i]:
            continue
        else:
            answer += 'no'
            break
    if answer == '':
        print('yes')
    else:
        print(answer)