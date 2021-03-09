n = int(input())
if n in [1, 3]:
    answer = -1
elif (n%5)%2 == 0:
    answer = n//5 + (n%5)//2
else:
    answer = ((n//5)-1) + ((n%5+5)//2)
print(answer)