for _ in range(int(input())):
    n = int(input())
    s1 = input()
    s2 = input()
    answer = 0
    list1, list2 = [], []
    for i in range(n):
        if s1[i] != s2[i]:
            list1.append(s1[i])
            list2.append(s2[i])
    list1 = sorted(list1)
    list2 = sorted(list2)
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            answer += 0.5
        else:
            answer += 1
    print(int(answer))
