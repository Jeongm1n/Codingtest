n = int(input())
drinks = list(map(int, input().split()))
drinks.sort()
max_value = drinks[len(drinks)-1]
while len(drinks) > 1:
    max_value += (drinks[0]/2)
    drinks.pop(0)
print(max_value)