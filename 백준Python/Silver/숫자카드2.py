from sys import stdin
n = int(input())
card_n = list(map(int, stdin.readline().split()))
m = int(input())
card_m = list(map(int, stdin.readline().split()))
dic = dict()
for element in card_n:
    try:
        dic[element] += 1
    except:
        dic[element] = 1
for element in card_m:
    try:
        print(dic[element], end=' ')
    except:
        print(0, end=' ')