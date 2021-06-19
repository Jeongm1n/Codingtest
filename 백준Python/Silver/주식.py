for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    answer, maxValue = 0, 0
    for i in range(len(data) - 1, -1, -1):
        if data[i] > maxValue:
            maxValue = data[i]
        else:
            answer += maxValue - data[i]
    print(answer)
