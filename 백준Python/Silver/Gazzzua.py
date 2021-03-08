n = int(input())
coins = list(map(int, input().split()))
max_value = max(coins)
answer = 0
while 1:
    if coins[0] >= max_value:
        coins.pop(0)
        if len(coins) == 0:
            break
        max_value = max(coins)
    else:
        answer += (max_value-coins[0])
        coins.pop(0)
print(answer)