for _ in range(int(input())):
    n, m = map(int, input().split())
    doc = list(map(int, input().split()))
    idx = [i for i in range(len(doc))]
    length = len(doc)
    temp = doc[m]
    answer = 0
    while 1:
        x, y = doc.pop(0), idx.pop(0)
        answer += 1
        if len(doc) == 0:
            answer = length
            break
        if x < max(doc):
            doc.append(x)
            idx.append(y)
            answer -= 1
        if x >= max(doc) and (x == temp and y == m):
            break
    print(answer)