n, m = map(int, input().split())
card = list(map(int, input().split()))
card.sort()
cnt = 0

while cnt < m:
    cnt += 1
    temp = card[0] + card[1]
    card[0], card[1] = temp, temp
    card.sort()

print(sum(card))
