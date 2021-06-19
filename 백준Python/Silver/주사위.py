n = int(input())
data = list(map(int, input().split()))
answer = 0
temp = []
if n == 1:
    data = sorted(data)
    answer = sum(data[:5])
else:
    temp.append(min(data[0], data[5]))
    temp.append(min(data[1], data[4]))
    temp.append(min(data[2], data[3]))
    temp = sorted(temp)

    min1 = temp[0]
    min2 = temp[0] + temp[1]
    min3 = temp[0] + temp[1] + temp[2]

    n1 = (n - 2) * (n - 2) + 4 * (n - 1) * (n - 2)
    n2 = 4 * (n - 2) + 4 * (n - 1)
    n3 = 4

    answer += n1 * min1
    answer += n2 * min2
    answer += n3 * min3

print(answer)
