vowel = 'aAeEiIoOuU'
while 1:
    string = input()
    if string[0] == '#':
        break
    count = 0
    for element in string:
            if element in vowel:
                count += 1
    print(count)