string = input()
checkList = ['U', 'C', 'P', 'C']

for element in checkList:
    if element in string:
        idx = string.find(element)
        string = string[idx+1:]
        flag = True
    else:
        flag = False
        break
if flag == True:
    print('I love UCPC')
else:
    print('I hate UCPC')