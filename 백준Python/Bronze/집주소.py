while 1:
    number = input()
    if number == '0':
        break
    print((len(number)+1)+sum([2 if element == '1' else 4 if element == '0' else 3 for element in number]))