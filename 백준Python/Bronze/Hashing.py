alpha = 'abcdefghijklmnopqrstuvwxyz'
l = int(input())
string = input()
answer = 0
for i in range(len(string)):
    answer += ((alpha.index(string[i])+1) * (31**i))
print(answer % 1234567891)