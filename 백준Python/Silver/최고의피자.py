n = int(input())  # 토핑 종류의 수
a, b = map(int, input().split())  # 도우와 토핑의 가격
c = int(input())  # 도우의 열량
d = [int(input()) for _ in range(n)]  # 각 토핑의 열량
d.sort(reverse=True)
answer = c // a
cal = c
price = a
for i in range(n):
    cal += d[i]
    price += b
    temp = cal // price
    answer = max(answer, temp)
print(answer)
