i = 0
while 1:
    try:
        o, w = map(int, input().split())
        if o == 0:
            break
    except:
        exit()
    while 1:
        command, n = input().split()
        if command == '#':
            break
        if w <= 0:
            continue
        if command == 'F':
            w += int(n)
        elif command == 'E':
            w-= int(n)

    if w <= 0:
        i += 1
        print(i, 'RIP', sep=' ')
    elif w > o//2 and w < o*2:
        i += 1
        print(i, ':-)', sep=' ')
    else:
        i += 1
        print(i, ':-(', sep=' ')