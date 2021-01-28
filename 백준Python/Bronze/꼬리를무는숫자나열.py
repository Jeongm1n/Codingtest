n, m = map(int, input().split())
n -= 1
m -= 1 # 원점을 0으로 계산하기 위해
print(abs(n//4 - m//4) + abs(n%4 - m%4))