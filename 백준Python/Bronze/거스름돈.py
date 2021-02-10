coins = [500, 100, 50, 10, 5, 1]
price = int(input())
change = 1000 - price
answer = 0
for i in range(len(coins)):
    if change // coins[i] >= 1:
        answer += (change//coins[i])
        change %= coins[i]
print(answer)