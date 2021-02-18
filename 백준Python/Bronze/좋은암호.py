k, l = map(int, input().split())
min_value = 0
for i in range(2, l):
    if k % i == 0:
        min_value = i
        break
    
if min_value == 0:
    print('GOOD')
else:
    print('BAD', min_value)