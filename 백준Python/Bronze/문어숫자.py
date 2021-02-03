while 1:
    char = input()
    index = 0
    answer = 0
    if char[0] == '#':
        break
    length = len(char)-1
    for element in char:
        if element == '-':
            index = 0
        elif element == '\\':
            index = 1
        elif element == '(':
            index = 2
        elif element == '@':
            index = 3
        elif element == '?':
            index = 4
        elif element == '>':
            index = 5
        elif element == '&':
            index = 6
        elif element == '%':
            index = 7
        elif element == '/':
            index = -1
        answer += index * (8**length)
        length -= 1
    print(answer)