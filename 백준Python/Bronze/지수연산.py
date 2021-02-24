n = int(input())
answer = '{0:.300f}'.format(1/(2**n))
for i in range(len(answer)-1, 0, -1):
    if answer[i] != '0':
        index = i
        break

print(answer[:index+1])