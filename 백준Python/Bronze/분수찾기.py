x = int(input())
count = 0
while x > 0:
    x -= count
    count += 1    
x = count + x -1
answer = str(x) + '/' + str(count-x)
if count%2 == 0:
    answer = str(count-x) + '/' + str(x)
print(answer)
