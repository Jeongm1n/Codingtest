n = int(input())
cnt = 0
subtitle = 666
while 1:
    if '666' in str(subtitle):
        cnt += 1
    if cnt == n:
        print(subtitle)
        break
    subtitle += 1