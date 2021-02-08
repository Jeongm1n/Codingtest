from itertools import combinations
n, m = map(int, input().split())
cards = list(map(int, input().split()))
max_value = 0

for card in combinations(cards, 3):
    temp_value = sum(card)
    if max_value < temp_value and temp_value <= m:
        max_value = temp_value
print(max_value)