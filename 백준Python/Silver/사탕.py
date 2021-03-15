for _ in range(int(input())):
    j, n = map(int, input().split())
    box = []
    answer = 0
    for _ in range(n):
        r, c = map(int, input().split())
        box.append(r*c)
    while j > 0:
        j -= max(box)
        box.pop(box.index(max(box)))
        answer += 1
    print(answer)