while 1:
    leaf = 1
    branch = list(map(int, input().split()))
    if branch[0] == 0:
        break
    for i in range(1, branch[0]+1):
        leaf *= branch[2*i-1]
        leaf -= branch[2*i]
    print(leaf)